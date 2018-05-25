from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import  User
from AppTwo.forms import userform


# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    dict = {'help': 'Help Page'}
    return render(request, 'help.html', context = dict)

def users(request):
    dict = {'users': User.objects.order_by('last_name')}
    return render(request, 'users.html', context = dict)

def form(request):
    form = userform()
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return users(request)
        else:
            print('Error: Form is invalid')
    return render(request, 'form.html', context = {'userform':form})