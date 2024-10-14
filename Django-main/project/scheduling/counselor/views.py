from django.contrib.auth.admin import User
from django.shortcuts import render

#log in page
# backend


def home(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/home.html' , context)

def test(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/test.html' , context)

def master(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/master.html' , context)

def issues(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/issues.html' , context)

def accounts(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/accounts.html' , context)

def pa(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/pa.html' , context)

def map(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/map.html' , context)

def classes(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Counselor', 'name': 'Alejo'}
    return render(request, 'counselorfile/classes.html' , context)
