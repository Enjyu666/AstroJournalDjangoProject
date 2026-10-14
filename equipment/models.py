from django.db import models

class Equipment(models.Model):

    class EquipmentTypeChoice(models.TextChoices):
        TELESCOPE = 'Telescope', 'Telescope'
        BINOCULARS = 'Binoculars', 'Binoculars'
        CAMERA = 'Camera', 'Camera'
        SMARTPHONE = 'Smartphone', 'Smartphone'

    name = models.CharField(max_length=100)
    equipment_type = models.CharField(
        max_length=100,
        choices=EquipmentTypeChoice.choices
    )
    brand = models.CharField(
        max_length=50,
        blank=True
    )
    equipment_specs = models.CharField(
        max_length=100,
        blank=True
    )
    accessories = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.name