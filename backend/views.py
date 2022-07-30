from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import InputForm, VectorForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
import json
import requests

ngrok_flask_execute = "https://613a-2601-646-8a00-8430-00-84e3.ngrok.io/execute"
ngrok_flask_policy = "https://f33a-2601-647-5580-8930-00-9169.ngrok.io/runPolicy"

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
    print(type(request.POST.dict()["list_of_commands"]))
    array_commands = request.POST.dict()["list_of_commands"].split(",")
    json_list = json.dumps(array_commands)
    print(list_of_commands)
    print(type(list_of_commands))
    print("JSON LIST")
    print(json_list)
    print(type(json_list))
    # print(array_commands.tolist())
    # list_of_commands = list(crequest.POST.dict()["list_of_commands"].items())
    jsonData = {
        # "number_of_robots": 1,
        # "number_of_loops": 2,
        "number_of_robots": request.POST.dict()["number_of_robots"],
        "number_of_loops": request.POST.dict()["number_of_loops"],
        "commands": request.POST.dict()["list_of_commands"]
        # "commands": "roll;90;60;1,roll;180;60;1"
    }
    # jsonData = json.dumps(request.POST.dict()[""])
    # jsonData = json.dumps(customer_data)
    print("JSON DATAIS")
    print(jsonData)
    return send_flask_data(jsonData, ngrok_flask_execute)
    # return HttpResponse(request.POST.dict()["number_of_robots"])

@csrf_exempt
def save_vector_data(request):
    print(request.body)
    print(request.POST.dict())
    vector_data = {
        "id": request.POST.dict()["vector_text_box"]
    }
    jsonData = json.dumps(vector_data)
    print("JSON DATA")
    print(jsonData)

    # return HttpResponse(request.POST.dict()["vector_text_box"])
    return (send_flask_data(request.POST.dict(), ngrok_flask_policy))
    

def send_flask_data(json_data, ngrok_hostname):
    response = requests.post(ngrok_hostname, json=json_data)
    print("Response")
    print(response.status_code)
    return HttpResponse(response, content_type="application/json")
    # return response.content