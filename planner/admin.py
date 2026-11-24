from django.contrib import admin

from planner.models import ObservationPlan, ObservationTarget


@admin.register(ObservationPlan)
class ObservationPlanAdmin(admin.ModelAdmin):
    ...


@admin.register(ObservationTarget)
class ObservationTargetAdmin(admin.ModelAdmin):
    ...