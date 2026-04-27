from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Announcement, AnnouncementRead, Comment, Reaction
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'announcements/announcements_list.html'
    context_object_name = 'announcements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check which announcements the user has read
        if self.request.user.is_authenticated:
            read_ids = AnnouncementRead.objects.filter(user=self.request.user).values_list('announcement_id', flat=True)
            context['read_announcement_ids'] = list(read_ids)
            
            # Check which announcements the user has reacted to
            reacted_ids = Reaction.objects.filter(user=self.request.user).values_list('announcement_id', flat=True)
            context['reacted_announcement_ids'] = list(reacted_ids)
        return context

class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'image']
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcements_list')

    def test_func(self):
        return self.request.user.role in ['ADMIN', 'INSTRUCTOR']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
@require_POST
def toggle_read(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    read, created = AnnouncementRead.objects.get_or_create(user=request.user, announcement=announcement)
    if not created:
        read.delete()
        status = 'unread'
    else:
        status = 'read'
    return JsonResponse({'status': status, 'count': announcement.reads.count()})

@login_required
@require_POST
def toggle_reaction(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    reaction, created = Reaction.objects.get_or_create(user=request.user, announcement=announcement)
    if not created:
        reaction.delete()
        status = 'removed'
    else:
        status = 'added'
    return JsonResponse({'status': status, 'count': announcement.reactions.count()})

@login_required
@require_POST
def add_comment(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    text = request.POST.get('text')
    if text:
        comment = Comment.objects.create(user=request.user, announcement=announcement, text=text)
        return JsonResponse({
            'status': 'success',
            'user': comment.user.first_name or comment.user.username,
            'text': comment.text,
            'date': comment.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return JsonResponse({'status': 'error', 'message': _('El comentario no puede estar vacío.')}, status=400)
