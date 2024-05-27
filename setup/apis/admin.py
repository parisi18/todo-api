from django.contrib import admin
from .models import *

admin.site.register(ToDoList)

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'completed')
    list_filter = ('completed', 'date')
    search_fields = ('title', 'description')
    list_per_page = 25
    ordering = ['completed', 'date']