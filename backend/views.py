from json import JSONEncoder
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.


@api_view(['GET'])
def getEmployees(request):
    Employee1 = Employee.objects.all()
    Serializer = EmployeeSerializer(Employee1, many=True)
    return Response(Serializer.data)