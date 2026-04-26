import uuid
import bcrypt
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Challenge(models.Model):
    CATEGORY_CHOICES = [
        ('forensics', _('Forensics')),
        ('web', _('Web')),
        ('reversing', _('Reversing')),
        ('crypto', _('Cryptography')),
        ('pwn', _('Pwn')),
        ('misc', _('Miscellaneous')),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(help_text=_("HTML or Markdown content"))
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    flag_hash = models.CharField(max_length=128)
    flag_case_sensitive = models.BooleanField(default=True)
    flag_regex = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField(default=100)
    dynamic_scoring = models.BooleanField(default=False)
    hints = models.JSONField(default=list, blank=True, help_text=_('[{"text": "...", "cost_points": 0}, ...]'))
    attachments = models.JSONField(default=list, blank=True, help_text=_('List of URLs to files'))
    external_resource_url = models.URLField(blank=True, null=True, help_text=_("Genially/Google Sites URL"))
    is_published = models.BooleanField(default=False)
    time_limit_seconds = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='challenges_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_flag(self, raw_flag):
        salt = bcrypt.gensalt()
        self.flag_hash = bcrypt.hashpw(raw_flag.encode('utf-8'), salt).decode('utf-8')

    def check_flag(self, raw_flag):
        return bcrypt.checkpw(raw_flag.encode('utf-8'), self.flag_hash.encode('utf-8'))

    def __str__(self):
        return self.title

class Submission(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    flag_submitted = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    points_awarded = models.IntegerField(default=0)
    solved_at = models.DateTimeField(auto_now_add=True)
    time_taken_seconds = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-solved_at']

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    criteria_json = models.JSONField(help_text=_("Logic for unlocking this badge"))

    def __str__(self):
        return self.name

class StudentProgress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ctf_progress')
    total_points = models.IntegerField(default=0)
    solved_challenges = models.ManyToManyField(Challenge, blank=True, related_name='solvers')
    badges = models.ManyToManyField(Badge, blank=True, related_name='earners')

    def __str__(self):
        return f"Progress for {self.user.username}"
