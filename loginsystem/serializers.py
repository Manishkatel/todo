from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "created_at", "datecompleted", "user"]
        read_only_fields = ["user"]  # Prevents user from being modified

        
