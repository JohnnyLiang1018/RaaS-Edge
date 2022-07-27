from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import InputForm, VectorForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
import json
import requests

ngrok_flask_hostname = ""

class InputFormCreateView(CreateView):
    model = InputForm
    fields = ('number_of_robots', 'number_of_loops', 'list_of_commands')

    def get_form(self, form_class=None):
        form = super(InputFormCreateView, self).get_form(form_class)
        form.fields['number_of_robots'].required = True
        form.fields['number_of_loops'].required = True
        form.fields['list_of_commands'].required = True

        return form

class VectorFormCreateView(CreateView):
    model = VectorForm
    fields = ('vector_text_box',)

    def get_form(self, form_class=None):
        form = super(VectorFormCreateView, self).get_form(form_class)
        form.fields['vector_text_box'].required = True

        return form

def home(request):
    return render(request, 'homepage.html')

@csrf_exempt
def save_robot_actions(request):
    print(request.body)
    print(request.POST.dict())
    jsonData = json.dumps(request.POST.dict())
    # return send_flask_data(jsonData)
    return HttpResponse(request.POST.dict()["number_of_robots"])

@csrf_exempt
def save_vector_data(request):
    print(request.body)
    print(request.POST.dict())
    vector_data = {
        "id": request.POST.dict()["vector_text_box"]
    }
    jsonData = json.dumps(vector_data)
    return HttpResponse(request.POST.dict()["vector_text_box"])
    # return (send_flask_data(request.POST.dict()[]))
    

def send_flask_data(json_data):
    response = requests.post(ngrok_flask_hostname, json=json_data)
    return HttpResponse(response, content_type="application/json")
    # return response.content