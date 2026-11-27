from django.contrib.auth.models import AbstractUser
from django.db import models

from objects.models import CelestialObject


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='user_profile_images/'
    )
    is_public = models.BooleanField(default=False)

    favourite_objects = models.ManyToManyField(
        CelestialObject,
        blank=True,
        related_name='favourited_by'
    )