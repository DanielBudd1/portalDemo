from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
import urllib3
import certifi
from base64 import b64encode

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
    employee1 = Employee.objects.get(id=pk)
    Employee.delete()
    return Response('Note was deleted.')





def postToAppian():
    http = urllib3.PoolManager(ca_certs=certifi.where())

    payload = {'name': 'John Doe'}
    # encoded_data = json.dumps(payload).encode('utf-8')
    encoded_data = b64encode(open('test_book.xlsx', 'rb').read()),
    resp = http.request(
        'POST',
        'https://convedodev.appiancloud.com/suite/webapi/hHAFeg',
        body=encoded_data,
        headers={'Appian-API-Key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4ZmI4ZjU3Zi00NTkzLTRjM2EtODc5Yy00NWVlY2Y1ZDM5MDgifQ.vBsGgPP9cfR0BvRfECUXVv2rctfXrE7zhC-DDkckDqc'})

    data = resp.data.decode('utf-8')
    return(data)
