from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_activated = models.BooleanField(default=False)

    # Add related_name arguments to the definitions of groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
        related_name='customuser_set',  # Add this line
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
        related_name='customuser_set',  # Add this line
    )