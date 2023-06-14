from django.forms import ModelForm
from .models import Medication

class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['name_of_medication', 'picture', 'times_per_day', 'dosage', 'unit']


