from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ...


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ...