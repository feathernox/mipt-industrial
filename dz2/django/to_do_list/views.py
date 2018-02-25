from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import ToDoItem

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    error = request.GET.get('error')
    context = {'error': error}
    return render(request, 'login.html', context)

def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        response = redirect('login_view')
        response['Location'] += '?error=true'
        return response
    else:
        login(request, user)
        return redirect('index')

def signup_view(request):
    error = request.GET.get('error')
    context = {'error': error}
    return render(request, 'signup.html', context)

def signup_action(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username, password=password)
    except IntegrityError:
        response = redirect('signup_view')
        response['Location'] += '?error=true'
        return response
    user.save()
    login(request, user)
    return redirect('index')

def logout_action(request):
    logout(request)
    return redirect('index')

@login_required
def todolist_view(request):
    query = ToDoItem.objects.filter(user=request.user).order_by('date')
    context = {'todo_items': query}
    return render(request, 'todolist.html', context)

@login_required
def todolist_action_add(request):
    item = request.POST['todoitem']
    ToDoItem(user=request.user, text=item).save()
    return redirect('todolist_view')

@login_required
def todolist_action_update(request):
    query = ToDoItem.objects.filter(user=request.user)
    for todo_item in query:
        todo_item.check = str(todo_item.id) in request.POST
        todo_item.save()
        if str(todo_item.id) + '_delete' in request.POST:
            todo_item.delete()
    return redirect('todolist_view')
