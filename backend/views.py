from django.http import HttpResponse
from django.shortcuts import render
from .models import InputForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

class InputFormCreateView(CreateView):
    model = InputForm
    fields = ('number_of_robots', 'number_of_loops', 'list_of_commands')

    def get_form(self, form_class=None):
        form = super(InputFormCreateView, self).get_form(form_class)
        form.fields['number_of_robots'].required = True
        form.fields['number_of_loops'].required = True
        form.fields['list_of_commands'].required = True

        return form

def home(request):
    return render(request, 'homepage.html')

# @csrf_exempt
# def save_robot_actions(request):
#     print(request.body)
#     print(request.POST.dict())
#     return HttpResponse(request.POST.dict()["number_of_robots"])
