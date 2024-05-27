from django.contrib import admin

from .models import ToDo

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'completed')
    list_filter = ('completed', 'date')
    search_fields = ('title', 'description')
    ordering = ['completed', 'date']
    list_per_page = 25
    
admin.site.register(ToDo, ToDoListAdmin)