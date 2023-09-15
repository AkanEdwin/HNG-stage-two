from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from . models import Persons
from . serializers import PersonsSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list':'/persons/',
        'Detail View':'/persons-detail/<str:pk>/',
        'Create':'/persons-create/',
        'Update':'/persons-update/<str:pk>/',
        'Delete':'/persons-delete/<str:pk/',
    }

    return Response(api_urls)

@api_view(['GET'])
def personsList(request):
    persons = Persons.objects.all()
    serializer = PersonsSerializer(persons, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def personsDetail(request, pk):
    persons = Persons.objects.get(id=pk)
    serializer = PersonsSerializer(persons, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def personsCreate(request):
    serializer = PersonsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def personsUpdate(request, pk):
    persons = Persons.objects.get(id=pk)
    serializer = PersonsSerializer(instance=persons, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def personsDelete(request, pk):
    persons = Persons.objects.get(id=pk)
    persons.delete()
    

    return Response("Item successfully deleted")

