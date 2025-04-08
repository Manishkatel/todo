from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    list_display = ('title', 'memo', 'important', 'created', 'datecompleted')
    list_filter = ('created', 'datecompleted')
    ordering = ('-datecompleted',)  # Must be a tuple
    search_fields = ('title',)

admin.site.register(Todo, TodoAdmin) 


