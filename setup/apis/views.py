from rest_framework import viewsets
from .serializers import TodoSerializer
from todo import models

# # Get
# class ListTodo(generics.ListAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = ToDoListSerializer

# # Update
# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = ToDoListSerializer

# # Create
# class CreateTodo(generics.CreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializers_class = ToDoListSerializer

# # Delete
# class DeleteTodo(generics.DestroyAPIView): 
#     queryset = models.Todo.objects.all()
#     serializers_class = ToDoListSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer