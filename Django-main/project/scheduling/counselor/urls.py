from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('counselor/', views.home, name = "counselorfile.home"), # making a list of data
    path('counselor/test/', views.test, name = "counselorfile.test"), # making a list of data
    path('counselor/master/', views.master, name = "counselorfile.master"),
    path('counselor/issues/', views.issues, name = "counselorfile.issues"),
    path('counselor/map/', views.map, name = "counselorfile.map"),
    path('counselor/pa/', views.pa, name = "counselorfile.pa"),
    path('counselor/accounts/', views.accounts, name = "counselorfile.accounts"),
    path('counselor/classes/', views.classes, name = "counselorfile.classes"),
]
