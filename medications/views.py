from django.shortcuts import render, redirect, get_object_or_404
from .models import Medication
from .forms import MedicationForm
from django.contrib.auth.decorators import login_required

@login_required
def all_medications(request):
    all = Medication.objects.all()
    return render(request, 'medication.html', {'medications': all})

@login_required
def new_medication(request):
    form = MedicationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_medications)

    return render(request, 'medication_form.html', {'form': form, 'new': True})

@login_required
def update_medication(request, id):
    medication = get_object_or_404(Medication, pk=id)

    form = MedicationForm(request.POST or None, request.FILES or None, instance=Medication)

    if form.is_valid():
        medication.save()
        return redirect(all_medications)

    return render(request, 'medication_form.html', {'form': form, 'new': False})

@login_required
def delete_medication(request, id):
    medication = get_object_or_404(Medication, pk=id)

    if request.method == "POST":
        medication.delete()
        return redirect(all_medications)

    return render(request, 'accept.html', {'medication': medication})
