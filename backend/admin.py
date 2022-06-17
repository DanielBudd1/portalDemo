from django.contrib import admin


# Register your models here.
from .models import Employee
# from import_export.admin import ImportExportModelAdmin
# from import_export import resources


admin.site.register(Employee)

