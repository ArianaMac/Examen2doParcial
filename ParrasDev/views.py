from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

@action(detail=False, methods=['get'])
def list_ids(self, request):
        ToDoList = ToDo.objects.values_list('id', flat=True)
        return Response(ToDoList)

@action(detail=False, methods=['get'])
def list_ids_titles(self, request):
        ToDoList = ToDo.objects.values('id', 'title')
        return Response(ToDoList)

@action(detail=False, methods=['get'])
def unresolved(self, request):
        ToDoList = ToDo.objects.filter(is_completed=False).values('id', 'title')
        return Response(ToDoList)

@action(detail=False, methods=['get'])
def resolved(self, request):
        ToDoList = ToDo.objects.filter(is_completed=True).values('id', 'title')
        return Response(ToDoList)

@action(detail=False, methods=['get'])
def list_ids_user_ids(self, request):
        ToDoList = ToDo.objects.values('id', 'user_id')
        return Response(ToDoList)

@action(detail=False, methods=['get'])
def resolved_user_ids(self, request):
        ToDoList = ToDo.objects.filter(is_completed=True).values('id', 'user_id')
        return Response(ToDoList)

@action(detail=False, methods=['get'])
def unresolved_user_ids(self, request):
        ToDoList = ToDo.objects.filter(is_completed=False).values('id', 'user_id')
        return Response(ToDoList)

    