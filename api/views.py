from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ClientSerializer, ClientInfoSerializer
from .models import Client, Project, User
# Create your views here.
# @api_view(['GET'])
# def apiOverview(request):
#     client_urls = {
#         'List' : '/clients/',
#         'Add Project':'/projects/',
#         'Update':'/clients/<int:id>',
#         'Delete client':' /clients/<int:id>',
        
#     }
#     return Response(client_urls)

@api_view(['GET'])
def listOfAllClients(request):
    clients = Client.objects.all()
    serialize = ClientSerializer(clients, many=True)
    return Response(serialize.data)

# @api_view(['GET'])
# def clientInfo(request,id):
#     client = Client.objects.get(id=id)
#     serialize = ClientInfoSerializer(client, many=False)
#     return Response(serialize.data)

class clientInfo(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientInfoSerializer
    lookup_field = 'id'
    
@api_view(['POST'])
def registerClient(request):
    serialize = ClientSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)

# @api_view(['PUT-PATCH'])
# def updateClient(request,id):
#     client = Client.objects.get(id=id)
#     serialize = ClientSerializer(instance=client, data=request.data)
#     if serialize.is_valid():
#         serialize.save()
#     return Response(serialize.data)

# class DeleteClient(generics.DestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientInfoSerializer
#     lookup_field = 'id'
@api_view(['DELETE'])
def deleteClient(request,id):
    client = Client.objects.get(id=id)
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)