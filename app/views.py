from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        print(request.POST)
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, uname + 'Logged in !')
            return redirect('home')
        else:
            messages.info(request, "Username or Password is Incorrect")


    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')


def register(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        # print(request.POST) This is for printing the data entered by user while registering
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'User Registered Successfully !.' + user)
            return redirect('login')
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context=context)
