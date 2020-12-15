from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.getDriversWithinDistance, name='getDriversWithinDistance'),
    path('add/', views.updateDrivesCoordinates, name='updateDrivesCoordinates'),
    path('driverlist/', views.getDrivers, name='getDrivers'),
]