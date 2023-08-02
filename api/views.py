from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        "login", "register"
    ] 
    return Response(routes)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)