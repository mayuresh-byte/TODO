import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, TodoForm, EditForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app.models import Todo
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def index(request):
    form = TodoForm()
    todos = Todo.objects.filter(user = request.user).order_by('priority')
    print(todos)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            print(form.cleaned_data)
            messages.success(request, 'Task Added !')
            return redirect('home')
        else:
            messages.info(request, 'Something Went Wrong !')
            return redirect('home')
    context = {'form':form, 'todos':todos}
    return render(request, 'index.html', context=context)

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


def deleteTodo(request, id):
    Todo.objects.get(id = id).delete()
    return redirect('home')

def editTodo(request, id):
    obj = Todo.objects.get(id = id)
    if(request.method == 'POST'):
        title = request.POST.get('title')
        obj.title = title
        obj.save()
        return redirect('home')

    return render(request, 'edit.html')
    