from django.shortcuts import render
from django.contrib.auth.admin import User

# Create your views here.


def login(request):
    users = User.objects.all()
    # context = {'users':users, 'role':'', 'name': ''}
    return render(request, 'loginfile/login.html')

