from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Project
from .serializers import ProjectSerializer

# Create your views here.
@api_view(['GET'])
def listProjects(request):
    clients = Project.objects.all()
    serialize = ProjectSerializer(clients, many=True)
    return Response(serialize.data)