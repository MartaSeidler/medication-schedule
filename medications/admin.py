from django.contrib import admin
from .models import Medication


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name_of_medication']
    list_filter = ['name_of_medication']
    search_fields = ['name_of_medication']


# admin.site.register(Capacity)
