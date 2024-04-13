from django.contrib.auth.models import AbstractUser
from django.db import models

class Teacher(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this teacher belongs to.',
        related_name='teachers_set',
        related_query_name='teacher',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this teacher.',
        related_name='teachers_set',
        related_query_name='teacher',
    )

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.username
