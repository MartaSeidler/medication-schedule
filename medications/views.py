from django.shortcuts import render
from django.http import HttpResponse

def all_medications(request):
    # return HttpResponse("Test")
    return render(request, 'medication.html')

