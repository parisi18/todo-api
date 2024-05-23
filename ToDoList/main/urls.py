from django.urls import path
from .views import  *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='detail_todo'),
    path('create/', CreateTodo.as_view(), name='create_todo'),
    path('', ListTodo.as_view(), name='list_todo'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete_todo'),
]
