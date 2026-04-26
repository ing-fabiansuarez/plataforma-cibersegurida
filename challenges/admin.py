from django.contrib import admin
from .models import Challenge, Submission, Badge, StudentProgress

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
    list_display = ('name', 'description')

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points')
    search_fields = ('user__username',)
