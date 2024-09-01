from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']
        
class ClientInfoSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(source='project_id', read_only=True)
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by','project']
        
    def update(self, instance, validated_data):
        # Update the Client instance with validated data
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        # You can include additional fields here if needed
        instance.save()
        return instance
