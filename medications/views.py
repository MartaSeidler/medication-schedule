from django.shortcuts import render
from .models import Medication


def all_medications(request):
    #all = Medication.objects.all()
    all = []
    return render(request, 'medication.html', {'medications': all})

