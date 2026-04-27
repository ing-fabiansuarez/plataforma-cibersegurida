from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", _("Administrador")
        INSTRUCTOR = "INSTRUCTOR", _("Instructor")
        STUDENT = "STUDENT", _("Estudiante")

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT
    )
    score = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def is_student(self):
        return self.role == self.Role.STUDENT
