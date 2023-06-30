from django.urls import path
from .views import all_medications, new_medication, update_medication, delete_medication, medication_detail

urlpatterns = [
    path('', all_medications, name='all_medications'),
    path('all_medications/', all_medications, name='all_medications'),
    path('new_medication', new_medication, name='new_medication'),
    path('update_medication/<int:id>/', update_medication, name='update_medication'),
    path('delete_medication/<int:id>/', delete_medication, name='delete_medication'),
    path('<slug:medication>/', medication_detail, name='medication_detail'),
]
