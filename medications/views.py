from django.shortcuts import render, redirect, get_object_or_404
from .models import Medication, Dose
from .forms import MedicationForm, CreateUserForm, DoseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def all_medications(request):
    all = Medication.objects.all()
    return render(request, 'medication.html', {'medications': all})


@login_required
def medication_detail(request, medication):
    medication = get_object_or_404(Medication, slug=medication)
    doses = medication.doses.filter(active=True)

    if request.method == 'POST':
        dose_form = DoseForm(data=request.POST)
        if dose_form.is_valid():
            new_dose = dose_form.save(commit=False)
            new_dose.medication = medication
            new_dose.save()
    else:
        dose_form = DoseForm()

    return render(request, 'detail.html', {'medication': medication, 'doses': doses, 'dose_form': dose_form})


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

    form = MedicationForm(request.POST or None, request.FILES or None, instance=medication)

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

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account created")

            return redirect(all_medications)

    return render(request, 'registration/register.html', {'form': form})