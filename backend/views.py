from json import JSONEncoder
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from yaml import serialize
from .serializers import EmployeeSerializer, FileSerializer
from .models import Employee 
from .utils import createEmployee, getEmployeeDetails, getEmployeesDetails, updateEmployee, deleteEmployee
from tablib import Dataset
import os

# Create your views here.

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['GET'])
def successfulUpload(request):
    if request.method == 'GET':
        os.remove(r'CSVs/test_book.xlsx')
        return Response('xlsx file was deleted.')


@api_view(['GET','POST'])
def getEmployees(request):
    if request.method == 'GET':
        return Response(getEmployeesDetails(request))

    elif request.method == 'POST':
        return Response(createEmployee(request))

@api_view(['GET','PUT','DELETE'])
def getEmployee(request, pk):
    if request.method == 'GET':
        return Response(getEmployeeDetails(request, pk))

    elif request.method == 'PUT':
        return Response(updateEmployee(request, pk))

    elif request.method == 'DELETE':   
        return Response(deleteEmployee(request, pk))
    
    else:
        pass

