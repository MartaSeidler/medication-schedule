from django.contrib import admin
from .models import Medication, Dose


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name_of_medication', 'slug']
    list_filter = ['name_of_medication']
    search_fields = ['name_of_medication']
    prepopulated_fields = {'slug': ('name_of_medication',)}


@admin.register(Dose)
class DoseAdmin(admin.ModelAdmin):
    list_display = ['medication', 'time', 'dosage', 'unit']
    list_filter = ['medication', 'time']
    search_fields = ['medication']
