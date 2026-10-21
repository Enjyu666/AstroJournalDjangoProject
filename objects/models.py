from django.core.validators import MinLengthValidator
from django.db import models

class CelestialObject(models.Model):

    class ObjectTypeChoice(models.TextChoices):
        PLANET = 'Planet', 'Planet'
        STAR = 'Star', 'Star'
        CONSTELLATION = 'Constellation', 'Constellation'
        SATELLITE = 'Satellite', 'Satellite'
        CLUSTER = 'Cluster', 'Cluster'
        NEBULA = 'Nebula', 'Nebula'
        COMET = 'Comet', 'Comet'
        GALAXY = 'Galaxy', 'Galaxy'

    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2)
        ]
    )
    object_type = models.CharField(
        max_length=100,
        choices=ObjectTypeChoice.choices
    )
    description = models.TextField(
        max_length=200,
        blank=True,
    )

    image = models.ImageField(
        upload_to='celestial_object_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name