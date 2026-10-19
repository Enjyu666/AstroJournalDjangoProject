from django.shortcuts import render

from objects.models import CelestialObject


def home(request):

    has_objects = CelestialObject.objects.exists()

    context = {
        'has_objects': has_objects
    }

    return render(request, 'home.html', context)


