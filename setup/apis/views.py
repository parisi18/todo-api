from rest_framework import viewsets
from .serializers import TodoSerializer
from todo.models import ToDo
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ToDo class"""
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
