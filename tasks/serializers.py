from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_status(self, value):
        if value not in [choice[0] for choice in Task.TaskStatus.choices]:
            raise serializers.ValidationError('Недопустимый статус задачи')
        return value