from django.shortcuts import redirect, render
from django.contrib.auth.admin import User
from django.http import JsonResponse

from .forms import RedirectForm
# Create your views here.

#log in 
# backend




# def home(request):
#     users = User.objects.all()
#     context = {'users':users, 'role':'Administration', 'name': 'Josh'}
#     return render(request, 'adminfile/home.html' , context)

def test(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh'}
    return render(request, 'adminfile/test.html' , context)

def master(request):
    # users = User.objects.all()
    # context = {'users':users, 'role':'Administration', 'name': 'Josh', 'teacher' : [1,2,3,4,5,6,7,8,9,10,11], 'n' : range(10),}
    context = {}
    print(request.method)
    if request.method == 'POST':
        form = RedirectForm(request.POST)
        if form.is_valid():
            period = form.cleaned_data['select_period']
            context['period'] = period
            return redirect('adminfile.master_id', id=period)
    else:
        form = RedirectForm()
    context['form'] = form
    context['user'] = User.objects.get(username='miner_910121')
    context['role'] = 'Administration'
    context['name'] = "Josh"
    return render(request, 'adminfile/master.html' , context)

# def master(request, id):
#     # users = User.objects.all()
#     # context = {'users':users, 'role':'Administration', 'name': 'Josh', 'teacher' : [1,2,3,4,5,6,7,8,9,10,11], 'n' : range(10),}
#     context = {}
#     print(request.method)
#     if request.method == 'POST':
#         form = RedirectForm(request.POST)
#         if form.is_valid():
#             period = form.cleaned_data['select_period']
#             context['period'] = period
#             return redirect('adminfile.master_id', id=period)
#     else:
#         form = RedirectForm()
#     context['form'] = form
#     context['user'] = User.objects.get(username='miner_910121')
#     context['role'] = 'Administration'
#     return render(request, 'adminfile/master.html' , context)


# def my_view(request):
#     sort_order = request.GET.get('sort', 'default_sort_order')
#     if sort_order == 'all':
#         data = masterSchedule.objects.all().order_by('my_field')
#     elif sort_order == 'zero':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '1st':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '2nd':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '3rd':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '4th':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '5th':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '6th':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '7th':
#         data = MyModel.objects.all().order_by('my_field')
#     elif sort_order == '8th':
#         data = MyModel.objects.all().order_by('my_field')
#     else:
#      data = MyModel.objects.all()  # Default sorting

    # Render your template with the sorted data
   # return render(request, 'master.html', {'data': data})

def home(request):
    context = {}
    print(request.method)
    if request.method == 'POST':
        form = RedirectForm(request.POST)
        if form.is_valid():
            period = form.cleaned_data['select_period']
            context['period'] = period
            return redirect('index', id=period)
    else:
        form = RedirectForm()
    context['form'] = form
    context['user'] = User.objects.get(username='miner_910121')
    context['role'] = 'Administration'

    return render(request, 'adminfile/home.html',context)

def masterTeachers(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh', 'teachers' :[1,2,3,4,5,6,7,8,9,10,11], 'n' : range(10),}
    return render(request, 'adminfile/masterTeachers.html' , context)

def classes(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh', 'classes':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    return render(request, 'adminfile/classes.html' , context)

def issues(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh'}
    return render(request, 'adminfile/issues.html' , context)

def accounts(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh'}
    return render(request, 'adminfile/accounts.html' , context)


def map(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh'}
    return render(request, 'adminfile/map.html' , context)

def oldSchedule(request):
    users = User.objects.all()
    context = {'users':users, 'role':'Administration', 'name': 'Josh'}
    return render(request, 'adminfile/oldSchedule.html' , context)
