from django.contrib import admin
from .models import Announcement, AnnouncementRead, Comment, Reaction

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ReactionInline(admin.TabularInline):
    model = Reaction
    extra = 0

class ReadInline(admin.TabularInline):
    model = AnnouncementRead
    extra = 0
    readonly_fields = ('user', 'read_at')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'read_count', 'like_count')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    inlines = [CommentInline, ReactionInline, ReadInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)
