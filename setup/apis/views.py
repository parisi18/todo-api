from rest_framework import viewsets
from .serializers import TodoSerializer
from todo.models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
