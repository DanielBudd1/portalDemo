from inspect import getcoroutinestate
from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.getEmployees, name="employees"),
    # path('employees/<str:pk>/update', views.updateEmployee, name='update-employee'),
    # path('employees/create', views.createEmployee, name='create-employee'),
    # path('employees/<str:pk>/delete', views.deleteEmployee, name='delete-employee'),
    path('employees/<str:pk>/', views.getEmployee, name='Employee'),

]