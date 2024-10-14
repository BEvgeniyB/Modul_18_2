from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class class_task2(TemplateView):
    template_name = "class_task2.html"

def function_task2(request):
    return render(request,"function _task2.html")

