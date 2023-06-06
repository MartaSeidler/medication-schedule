from django.contrib import admin
from .models import Medication

#admin.site.register(Medication)

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name_of_medication', 'capacity', 'start_date']
    list_filter = ['name_of_medication', 'start_date']
    search_fields = ['name_of_medication']
