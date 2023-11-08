from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'avatars/{new_file_name}'


SEX_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female')
)

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(blank=True, upload_to = uniq_name_upload)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.IntegerField(null=True)
    location = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        error_messages={
            'add': 'The permission you are trying to add already exists for the user.',
            'remove': 'The permission you are trying to remove does not exist for the user.',
        },
    )


