from django.forms import ModelForm
from .models import Medication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['name_of_medication', 'picture', 'time_1', 'dosage_1', 'unit_1', 'time_2', 'dosage_2', 'unit_2', 'time_3', 'dosage_3', 'unit_3']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']