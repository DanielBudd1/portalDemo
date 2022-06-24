from json import JSONEncoder
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from yaml import serialize
from .serializers import EmployeeSerializer, FileSerializer
from .models import Employee 
from .utils import compareStructures, createEmployee, getEmployeeDetails, getEmployeesDetails, postToAppian, updateEmployee, deleteEmployee
from tablib import Dataset
import os
import pandas as pd


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser,) 
  permission_classes = (IsAuthenticated,)
  

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    file_location = "CSVs/test_book.xlsx"
    control_file_location = 'example_file.xlsx'
    if file_serializer.is_valid():
        file_serializer.save()
        uploaded_data_frame = pd.read_excel(file_location)
        comparison_results = compareStructures(control_file_location, uploaded_data_frame)
        if comparison_results == "Invalid Format":
            os.remove(file_location)
            return Response("Incorrect File Format")
        elif comparison_results == "Null Values Present":
            os.remove(file_location)
            return Response("Null Values Present")
        else:
            appian_pm_results = postToAppian(uploaded_data_frame)
            if appian_pm_results == "failed":
                os.remove(file_location)
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# api recievs exel file, compares it to control file, then posts to appian
 

@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def successfulUpload(request):
    os.remove("CSVs/test_book.xlsx")
    return Response('Successfully Deleted')
    
# when appian succesffuly processes file, it replies and deletes file


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

