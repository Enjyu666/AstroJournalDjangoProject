from django.db import models

from accounts.models import CustomUser
from objects.models import CelestialObject

#
# class ObservationPlan(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='observation_plans')
#     plan_name = models.CharField(max_length=50)
#     description = models.TextField(blank=True)
#     # scheduled_date = models.DateField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.plan_name
#


class ObservationTarget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='observation_targets')
    celestial_object = models.ForeignKey(CelestialObject, on_delete=models.PROTECT, related_name='observation_targets')
    scheduled_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.celestial_object.name