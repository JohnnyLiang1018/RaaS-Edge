from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')


def notebook(request):
    return render(request, 'notebook.html')
# Create your views here.
