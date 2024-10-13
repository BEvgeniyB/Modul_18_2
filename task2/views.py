from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def class_task2(request):
    return render(request,"class_task2.html")

def def_task2(request):
    return render(request,"def_task2.html")

# class Index(TemplateView):
#     template_name = 'index_task2'