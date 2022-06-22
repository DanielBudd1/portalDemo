from inspect import getcoroutinestate
from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.getEmployees, name="employees"),
    path('employees/<str:pk>/', views.getEmployee, name='Employee'),
    path('upload', views.FileView.as_view(),name="uploadxlsx"),
    path('uploadSuccessful', views.successfulUpload, name='successfulUpload') 

]