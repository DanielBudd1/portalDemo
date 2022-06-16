from json import JSONEncoder
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from .serializers import EmployeeSerializer
from .models import Employee
from .utils import createEmployee, getEmployeeDetails, getEmployeesDetails, updateEmployee, deleteEmployee
# Create your views here.


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
