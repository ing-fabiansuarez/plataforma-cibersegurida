from django.contrib import admin
from .models import Challenge, Submission, Badge, UserBadge, StudentProgress

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'points', 'is_published', 'created_at')
    list_filter = ('category', 'difficulty', 'is_published')
    search_fields = ('title', 'description')
    readonly_fields = ('id', 'created_at', 'updated_at')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('challenge', 'user', 'is_correct', 'points_awarded', 'solved_at')
    list_filter = ('is_correct', 'solved_at')
    search_fields = ('challenge__title', 'user__username', 'flag_submitted')

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'rarity', 'is_secret', 'points_awarded')
    list_filter = ('category', 'level', 'rarity', 'is_secret')
    search_fields = ('name', 'description')
    filter_horizontal = ('prerequisites',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'icon_url')
        }),
        ('Atributos', {
            'fields': ('category', 'subcategory', 'level', 'rarity', 'is_secret', 'points_awarded')
        }),
        ('Lógica de Desbloqueo', {
            'fields': ('conditions', 'prerequisites'),
            'description': 'Configura la lógica en formato JSON y las insignias previas requeridas.'
        }),
    )

@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'badge', 'earned_at')
    list_filter = ('earned_at', 'badge__rarity')
    search_fields = ('user__username', 'badge__name')

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points')
    search_fields = ('user__username',)
