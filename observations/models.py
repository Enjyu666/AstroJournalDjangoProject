from django.db import models

from equipment.models import Equipment
from objects.models import CelestialObject

class ObservationLog(models.Model):
    celestial_object = models.ForeignKey(CelestialObject, on_delete=models.CASCADE)
    date_observed = models.DateTimeField()
    location = models.CharField(
        max_length=100,
        blank=True
    )
    equipment = models.ManyToManyField(Equipment)
    notes = models.TextField(
        max_length=500,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)