# Create your views here.
from django.db import models
from django.views import generic
from django import requests
from django.shortcuts import render


class ListToDoClient(generic.View):
    template_name = "list_ToDo/list_ToDo_cl.html"
    context = {}
    url = "http://localhost:8000/api/4/ToDoList/"
    response = None

def get(self, request):
    self.response = requests.get(url=self.url)
    self.context = {
        "ToDoList" : self.response.json()
    }
    return render(request, self.template_name, self.context)

