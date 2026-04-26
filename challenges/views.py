from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Challenge, Submission, StudentProgress
from .forms import ChallengeForm, SubmissionForm

def is_instructor(user):
    return user.is_authenticated and (user.role == 'INSTRUCTOR' or user.is_superuser)

def is_student(user):
    return user.is_authenticated and user.role == 'STUDENT'

# Instructor Views
@login_required
@user_passes_test(is_instructor)
def instructor_challenge_list(request):
    challenges = Challenge.objects.filter(created_by=request.user)
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
            messages.success(request, 'Reto creado con éxito.')
            return redirect('instructor_challenge_list')
    else:
        form = ChallengeForm()
    return render(request, 'challenges/instructor/challenge_form.html', {'form': form, 'title': 'Crear Reto'})

@login_required
@user_passes_test(is_instructor)
def challenge_edit(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge = form.save(commit=False)
            if form.cleaned_data.get('flag_raw'):
                challenge.set_flag(form.cleaned_data.get('flag_raw'))
            challenge.save()
            messages.success(request, 'Reto actualizado con éxito.')
            return redirect('instructor_challenge_list')
    else:
        # We don't want to show the flag hash in the raw field
        form = ChallengeForm(instance=challenge)
        form.fields['flag_raw'].required = False
        form.fields['flag_raw'].help_text = "Deja en blanco para no cambiar la flag."
        
    return render(request, 'challenges/instructor/challenge_form.html', {
        'form': form, 
        'title': 'Editar Reto',
        'challenge': challenge
    })

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
                progress.save()
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
