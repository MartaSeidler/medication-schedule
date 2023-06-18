from django.forms import ModelForm
from .models import Medication



class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['name_of_medication', 'picture', 'time_1', 'dosage_1', 'unit_1', 'time_2', 'dosage_2', 'unit_2', 'time_3', 'dosage_3', 'unit_3']
