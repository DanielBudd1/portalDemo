from cgi import test
from cmath import e
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
import urllib3
import certifi
from base64 import b64encode
import pandas as pd
import os

# def createEmployee(request):
#     data = request.data
#     employee1 = Employee.objects.create(
#         body = data['body']
#     )
#     serializer = EmployeeSerializer(employee1, many=False)
#     return Response(serializer.data)

def getEmployeesDetails(request):
    Employee1 = Employee.objects.all()
    Serializer = EmployeeSerializer(Employee1, many=True)
    return (Serializer.data)

def createEmployee(request):
    data = request.data
    employee1 = Employee.objects.create(
        body = data['body']
    )
    serializer = EmployeeSerializer(employee1, many=False)
    return(serializer.data)


def getEmployeeDetails(request, pk):
    Employee1 = Employee.objects.get(id=pk)
    Serializer = EmployeeSerializer(Employee1, many=False)
    return Serializer.data


def updateEmployee(request, pk):
    data = request.data
    Employee1 = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=Employee1, data=data)
    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteEmployee(request, pk):
    """ functipm yo 
    """
    employee1 = Employee.objects.get(id=pk)
    Employee.delete()
    return Response('Note was deleted.')


def compareStructures(control_location, test_data_frame):
    control_data = pd.read_excel(control_location)
    try:
        differences = control_data.compare(test_data_frame)
    except:
        return("Invalid Format")
    if test_data_frame.isnull().values.any() == True:
        return("Null Values Present")
    else:
        return("successful")

# function takes location of comparison file and
# and dataframe and compairs the two for irregularities



def postToAppian(excel_data_df):
    http = urllib3.PoolManager(ca_certs=certifi.where())
    json_str = excel_data_df.to_json()
    encoded_data = json_str#.encode('utf-8')  appian currently does not decode the data
    print(encoded_data)
    resp = http.request(
        'POST',
        'https://convedodev.appiancloud.com/suite/webapi/fZdhLg',
        body=encoded_data,
        headers={'Appian-API-Key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4ZmI4ZjU3Zi00NTkzLTRjM2EtODc5Yy00NWVlY2Y1ZDM5MDgifQ.vBsGgPP9cfR0BvRfECUXVv2rctfXrE7zhC-DDkckDqc'})

    data = resp.data.decode('utf-8')
    return data

# function sends dataframe to appian as a json file