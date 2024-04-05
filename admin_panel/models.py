from django.contrib.auth.models import AbstractUser
from django.db import models

class Teacher(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='teachers_set',  # Added related_name
        related_query_name='teacher',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='teachers_set',  # Added related_name
        related_query_name='teacher',
    )

    def __str__(self):
        return self.username
