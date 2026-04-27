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

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"

class StudentProgress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ctf_progress')
    total_points = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    solved_challenges = models.ManyToManyField(Challenge, blank=True, related_name='solvers')

    def calculate_level(self):
        """Calcula el nivel basado en XP. Fórmula: nivel = floor(sqrt(xp / 100)) + 1"""
        import math
        new_level = math.floor(math.sqrt(self.xp / 100)) + 1 if self.xp > 0 else 1
        return new_level

    def add_xp(self, amount):
        self.xp += amount
        new_level = self.calculate_level()
        leveled_up = new_level > self.level
        self.level = new_level
        self.save()
        return leveled_up

    @property
    def xp_current_level(self):
        """XP acumulado en el nivel actual."""
        prev_level_xp = ((self.level - 1) ** 2) * 100
        return self.xp - prev_level_xp

    @property
    def xp_next_level(self):
        """XP total necesario para subir al siguiente nivel desde el inicio del nivel actual."""
        next_level_total = (self.level ** 2) * 100
        prev_level_xp = ((self.level - 1) ** 2) * 100
        return next_level_total - prev_level_xp

    @property
    def xp_percentage(self):
        """Porcentaje de progreso al siguiente nivel."""
        if self.xp_next_level == 0: return 0
        return min(int((self.xp_current_level / self.xp_next_level) * 100), 100)

    def __str__(self):
        return f"Progress for {self.user.username} (Lvl {self.level})"

# --- Badge System (Arquitectura Modular) ---

class Badge(models.Model):
    class Category(models.TextChoices):
        SKILL = "skill", _("Habilidad")
        ACHIEVEMENT = "achievement", _("Logro")
        COMPETITIVE = "competitive", _("Competitiva")
        SECRET = "secret", _("Secreta")

    class Level(models.IntegerChoices):
        BRONZE = 1, _("Bronce")
        SILVER = 2, _("Plata")
        GOLD = 3, _("Oro")
        PLATINUM = 4, _("Platino")

    class Rarity(models.TextChoices):
        COMMON = "common", _("Común")
        RARE = "rare", _("Rara")
        EPIC = "epic", _("Épica")
        LEGENDARY = "legendary", _("Legendaria")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.ACHIEVEMENT)
    subcategory = models.CharField(max_length=50, blank=True, help_text=_("Ej: web, crypto, etc."))
    level = models.IntegerField(choices=Level.choices, default=Level.BRONZE)
    rarity = models.CharField(max_length=20, choices=Rarity.choices, default=Rarity.COMMON)
    icon_url = models.URLField(blank=True, null=True)
    is_secret = models.BooleanField(default=False)
    points_awarded = models.IntegerField(default=0)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='unlocks')
    conditions = models.JSONField(
        default=dict, 
        blank=True, 
        help_text=_('JSON flexible: {"type": "solve_count", "category": "web", "count": 5}')
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='earned_badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name='awarded_to')
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'badge')
