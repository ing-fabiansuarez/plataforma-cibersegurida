from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Título"))
    content = models.TextField(verbose_name=_("Contenido"))
    image = models.ImageField(upload_to='announcements/', null=True, blank=True, verbose_name=_("Imagen"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements', verbose_name=_("Autor"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creado el"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Actualizado el"))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Anuncio")
        verbose_name_plural = _("Anuncios")

    def __str__(self):
        return self.title

    @property
    def read_count(self):
        return self.reads.count()

    @property
    def like_count(self):
        return self.reactions.count()

class AnnouncementRead(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='reads')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('announcement', 'user')

class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class Reaction(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, default='like')

    class Meta:
        unique_together = ('announcement', 'user')
