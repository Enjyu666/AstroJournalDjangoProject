from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.models import CustomUser, UserProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

        user_group = Group.objects.get(name='Catalogue Viewers')
        instance.groups.add(user_group)