from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response

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