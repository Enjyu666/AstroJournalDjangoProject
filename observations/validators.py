from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_not_future(value):
    if value > timezone.now():
        raise ValidationError(
            'One small step for an astronomer, one giant leap through time. Observations cannot come from the future.'
        )