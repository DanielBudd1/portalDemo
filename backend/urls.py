from inspect import getcoroutinestate
from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.getEmployees, name="routes")
]