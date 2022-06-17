from django.db import models

# Create your models here.
class Employee(models.Model): 
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name



class File(models.Model):
    file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)