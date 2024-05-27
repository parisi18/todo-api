from rest_framework import viewsets
from .serializers import TodoSerializer
from todo.models import ToDo

class TodoViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
