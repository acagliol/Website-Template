from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('administration/', views.home, name = "adminfile.home"),
    path('administration/test/', views.test, name = "adminfile.test"),
    # path('administration/master/<id>/', views.master, name = "adminfile.master_id"),
    path('administration/master/', views.master, name = "adminfile.master"),
    
    
    
    path('administration/masterTeachers/', views.masterTeachers, name = "adminfile.masterTeachers"),
    path('administration/issues/', views.issues, name = "adminfile.issues"),
    path('administration/map/', views.map, name = "adminfile.map"),
    path('administration/accounts/', views.accounts, name = "adminfile.accounts"),
    path('administration/oldSchedule/', views.oldSchedule, name = "adminfile.oldSchedule"),
    # path('administration/classes/<id>/', views.home, name = "adminfile.homie"),
    path('administration/classes/', views.classes, name = "adminfile.classes"),
]
