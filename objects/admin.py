from django.contrib import admin

from objects.models import CelestialObject


@admin.register(CelestialObject)
class CelestialObjectAdmin(admin.ModelAdmin):
    ...

