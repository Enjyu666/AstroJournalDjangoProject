from django.contrib import admin

from observations.models import ObservationLog, ObservationImage


@admin.register(ObservationLog)
class ObservationLogAdmin(admin.ModelAdmin):
    ...

@admin.register(ObservationImage)
class ObservationImageAdmin(admin.ModelAdmin):
    ...