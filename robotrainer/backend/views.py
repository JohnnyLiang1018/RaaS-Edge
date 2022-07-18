from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomJsonForm
from django import forms

def home(request):
    return render(request, 'homepage.html')


def notebook(request):
    return render(request, 'json_input.html', {'form': CustomJsonForm()} )
    # return render(request, 'notebook.html')
# Create your views here.
