from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializer import TodoSerializer

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

@api_view(['GET'])
def get_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

class todoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer