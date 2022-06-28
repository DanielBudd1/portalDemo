# from msilib.schema import File
from pyexpat import model
from rest_framework import serializers
from . models import Employee, File 

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employee
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file', 'timestamp')