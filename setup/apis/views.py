from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Get
class ListTodo(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

# Update
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

# Create
class CreateTodo(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    serializers_class = ToDoListSerializer

# Delete
class DeleteTodo(generics.DestroyAPIView): 
    queryset = ToDoList.objects.all()
    serializers_class = ToDoListSerializer