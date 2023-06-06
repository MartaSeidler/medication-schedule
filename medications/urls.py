from django.urls import path
from .views import all_medications

urlpatterns = [
    path('all_medications/', all_medications)
]
