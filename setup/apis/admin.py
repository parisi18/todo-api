from django.contrib import admin
from todo.models import Todo

admin.site.register(Todo)

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'completed')
    list_filter = ('completed', 'date')
    search_fields = ('title', 'description')
    list_per_page = 25
    ordering = ['completed', 'date']