from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django.utils.translation import gettext as _
import json
from .models import Challenge, Submission, StudentProgress, UserBadge, Badge
from .forms import ChallengeForm, SubmissionForm, BadgeForm

def is_instructor(user):
    return user.is_authenticated and (user.role == 'INSTRUCTOR' or user.is_superuser)

def is_student(user):
    return user.is_authenticated and user.role == 'STUDENT'

@login_required
@user_passes_test(is_instructor)
def instructor_badge_list(request):
    badges = Badge.objects.all().order_by('-created_at')
    return render(request, 'challenges/instructor/badge_list.html', {'badges': badges})

@login_required
@user_passes_test(is_instructor)
def badge_create(request):
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Insignia creada con éxito.'))
            return redirect('instructor_badge_list')
    else:
        # Pre-poblar si viene de un reto
        challenge_id = request.GET.get('challenge')
        initial_conditions = {}
        if challenge_id:
            initial_conditions = {"type": "specific_challenges", "challenge_ids": [challenge_id]}
        
        form = BadgeForm(initial={'conditions_json': json.dumps(initial_conditions)})
        
    return render(request, 'challenges/instructor/badge_form.html', {'form': form, 'title': _('Crear Insignia')})

@login_required
@user_passes_test(is_instructor)
def badge_edit(request, pk):
    badge = get_object_or_404(Badge, pk=pk)
    if request.method == 'POST':
        form = BadgeForm(request.POST, instance=badge)
        if form.is_valid():
            form.save()
            messages.success(request, _('Insignia actualizada con éxito.'))
            return redirect('instructor_badge_list')
    else:
        form = BadgeForm(instance=badge)
    return render(request, 'challenges/instructor/badge_form.html', {'form': form, 'title': _('Editar Insignia'), 'badge': badge})

@login_required
@user_passes_test(is_instructor)
def badge_delete(request, pk):
    badge = get_object_or_404(Badge, pk=pk)
    if request.method == 'POST':
        badge.delete()
        messages.success(request, _('Insignia eliminada con éxito.'))
        return redirect('instructor_badge_list')
    return render(request, 'challenges/instructor/badge_confirm_delete.html', {'badge': badge})
from .badges import BadgeEvaluator

# Instructor Views
@login_required
@user_passes_test(is_instructor)
def instructor_challenge_list(request):
    # Los instructores ven todos los retos, pero luego en la plantilla 
    # controlaremos qué pueden editar
    challenges = Challenge.objects.all().select_related('created_by').order_by('-created_at')
    return render(request, 'challenges/instructor/challenge_list.html', {'challenges': challenges})

@login_required
@user_passes_test(is_instructor)
def challenge_create(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.created_by = request.user
            # We need to handle the flag hashing here if not handled in form
            raw_flag = form.cleaned_data.get('flag_raw')
            challenge.set_flag(raw_flag)
            challenge.save()
            messages.success(request, _('Reto creado con éxito.'))
            return redirect('instructor_challenge_list')
    else:
        form = ChallengeForm()
    return render(request, 'challenges/instructor/challenge_form.html', {'form': form, 'title': _('Crear Reto')})

@login_required
@user_passes_test(is_instructor)
def challenge_edit(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    
    # Solo el creador o un superusuario puede editar
    if challenge.created_by != request.user and not request.user.is_superuser:
        messages.error(request, _('No tienes permiso para editar este reto porque fue creado por otro instructor.'))
        return redirect('instructor_challenge_list')

    if request.method == 'POST':
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge = form.save(commit=False)
            if form.cleaned_data.get('flag_raw'):
                challenge.set_flag(form.cleaned_data.get('flag_raw'))
            challenge.save()
            messages.success(request, _('Reto actualizado con éxito.'))
            return redirect('instructor_challenge_list')
    else:
        # We don't want to show the flag hash in the raw field
        form = ChallengeForm(instance=challenge)
        form.fields['flag_raw'].required = False
        form.fields['flag_raw'].help_text = _("Deja en blanco para no cambiar la flag.")
        
    return render(request, 'challenges/instructor/challenge_form.html', {
        'form': form, 
        'title': _('Editar Reto'),
        'challenge': challenge
    })

@login_required
@user_passes_test(is_instructor)
def instructor_challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    
    # Solo el creador o un superusuario puede ver los detalles internos
    if challenge.created_by != request.user and not request.user.is_superuser:
        messages.error(request, _('No tienes permiso para ver los detalles de este reto.'))
        return redirect('instructor_challenge_list')

    submissions = Submission.objects.filter(challenge=challenge).select_related('user').order_by('-solved_at')
    
    # Filtrar solo las correctas para el listado de "estudiantes que lo han resuelto"
    solvers = submissions.filter(is_correct=True)
    
    return render(request, 'challenges/instructor/challenge_detail.html', {
        'challenge': challenge,
        'submissions': submissions,
        'solvers': solvers,
    })

@login_required
@user_passes_test(is_instructor)
def challenge_delete(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    
    # Solo el creador o un superusuario puede eliminar
    if challenge.created_by != request.user and not request.user.is_superuser:
        messages.error(request, _('No tienes permiso para eliminar este reto.'))
        return redirect('instructor_challenge_list')

    if request.method == 'POST':
        challenge.delete()
        messages.success(request, _('Reto eliminado con éxito.'))
        return redirect('instructor_challenge_list')
    return render(request, 'challenges/instructor/challenge_confirm_delete.html', {'challenge': challenge})

# Student Views
@login_required
def student_challenge_list(request):
    challenges = Challenge.objects.filter(is_published=True)
    progress, _ = StudentProgress.objects.get_or_create(user=request.user)
    solved_ids = progress.solved_challenges.values_list('id', flat=True)
    
    return render(request, 'challenges/student/challenge_list.html', {
        'challenges': challenges,
        'solved_challenges': solved_ids,
        'user_progress': progress
    })

@login_required
def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk, is_published=True)
    is_solved = Submission.objects.filter(challenge=challenge, user=request.user, is_correct=True).exists()
    
    if request.method == 'POST' and not is_solved:
        form = SubmissionForm(request.POST)
        if form.is_valid():
            flag = form.cleaned_data.get('flag')
            is_correct = challenge.check_flag(flag)
            
            Submission.objects.create(
                challenge=challenge,
                user=request.user,
                flag_submitted=flag,
                is_correct=is_correct,
                points_awarded=challenge.points if is_correct else 0
            )
            
            if is_correct:
                progress, _ = StudentProgress.objects.get_or_create(user=request.user)
                progress.total_points += challenge.points
                progress.solved_challenges.add(challenge)
                
                # Sistema de XP: 1 XP por cada punto del reto + bono base de 50 XP
                xp_gain = challenge.points + 50
                leveled_up = progress.add_xp(xp_gain)
                
                if leveled_up:
                    messages.success(request, f'🔥 ¡SUBISTE DE NIVEL! Ahora eres Nivel {progress.level}')
                
                # Evaluar insignias
                evaluator = BadgeEvaluator(request.user)
                new_badges = evaluator.evaluate_all()
                for badge in new_badges:
                    # Las insignias también dan XP
                    if badge.points_awarded > 0:
                        progress.add_xp(badge.points_awarded)
                    messages.info(request, f'🏅 ¡Has desbloqueado una nueva insignia: {badge.name}!')
                
                messages.success(request, '¡Felicidades! Flag correcta.')
            else:
                messages.error(request, 'Flag incorrecta. Inténtalo de nuevo.')
            
            return redirect('challenge_detail', pk=pk)
    else:
        form = SubmissionForm()
        
    solve_count = Submission.objects.filter(challenge=challenge, is_correct=True).count()
        
    return render(request, 'challenges/student/challenge_detail.html', {
        'challenge': challenge,
        'form': form,
        'is_solved': is_solved,
        'solve_count': solve_count
    })

@login_required
def user_profile(request, username=None):
    if username:
        user = get_object_or_404(settings.AUTH_USER_MODEL, username=username)
    else:
        user = request.user
    
    progress, _ = StudentProgress.objects.get_or_create(user=user)
    earned_badges = UserBadge.objects.filter(user=user).select_related('badge').order_by('-earned_at')
    
    # Insignias bloqueadas (no secretas)
    earned_ids = earned_badges.values_list('badge_id', flat=True)
    locked_badges = Badge.objects.exclude(id__in=earned_ids).filter(is_secret=False)

    # Cálculo de maestría por categoría
    category_mastery = []
    solved_challenges = progress.solved_challenges.all()
    
    for cat_id, cat_label in Challenge.CATEGORY_CHOICES:
        total_in_cat = Challenge.objects.filter(category=cat_id, is_published=True).count()
        solved_in_cat = solved_challenges.filter(category=cat_id).count()
        
        percentage = 0
        if total_in_cat > 0:
            percentage = int((solved_in_cat / total_in_cat) * 100)
            
        category_mastery.append({
            'id': cat_id,
            'label': cat_label,
            'solved': solved_in_cat,
            'total': total_in_cat,
            'percentage': percentage
        })
    
    return render(request, 'users/profile.html', {
        'profile_user': user,
        'progress': progress,
        'earned_badges': earned_badges,
        'locked_badges': locked_badges,
        'category_mastery': category_mastery,
    })
