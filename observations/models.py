from django.db import models

from equipment.models import Equipment
from objects.models import CelestialObject
from observations.validators import validate_not_future


class ObservationLog(models.Model):
    celestial_object = models.ForeignKey(CelestialObject, on_delete=models.CASCADE)
    date_observed = models.DateTimeField(
        validators=[
            validate_not_future
        ]
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    equipment = models.ManyToManyField(Equipment)
    notes = models.TextField(
        max_length=500,
        blank=True
    )
    rating = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

