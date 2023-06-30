from django.forms import ModelForm
from .models import Medication, Dose
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['name_of_medication', 'picture']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DoseForm(ModelForm):
    class Meta:
        model = Dose
        fields = ['time', 'dosage', 'unit']