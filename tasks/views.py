from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, AddTaskForm, LoginForm, SearchForm
from .models import Tasks

@login_required()
def index(request):
    user = request.user
    tasks = Tasks.objects.filter(author=user).order_by('priority')
    print(tasks)
    form = AddTaskForm()
    search_form = SearchForm()
    return render(request, 'tasks/index.html', {'tasks': tasks, 'AddTaskForm': form, 'SearchForm': search_form})

def add_task(request):
    task = Tasks()
    user = User.objects.get(username=request.user)
    task.title = request.POST['title']
    task.author = user
    task.save()
    return HttpResponseRedirect('/')

def delete_task(request):
    task_id = None
    for key, value in request.POST.items():
        if value == "Delete":
            task_id = key
    if task_id:
        Tasks.objects.filter(id=task_id).delete()

    return redirect("/")


def update_task(request):
    print("Информация из запроса: ", request.POST)
    task_id = None
    for key, value in request.POST.items():
        if value == "Save":
            print(key)
            task_id = key
    if task_id:
        task_old = Tasks.objects.get(id=task_id)
        task_old.title = request.POST['title']
        task_old.save()

    return redirect("/")


def update_priority(request):
    data = request.POST
    task_id = data['taskId']
    new_priority = data['priority']
    task = Tasks.objects.get(id=task_id)
    task.priority = new_priority
    task.save()

    return redirect("/")
def register(request):
    print(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            print(user)
            if user is not None:
                login(request, user)
            else:
                print("Пользователь не найден")
            return redirect("/")

    else:
        form = LoginForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")

def search(request):
    search_title = request.POST['title']
    tasks = Tasks.objects.filter(title__icontains=search_title)
    search_form = SearchForm()
    form = AddTaskForm()
    return render(request, 'tasks/index.html', {'tasks': tasks, 'AddTaskForm': form, 'SearchForm': search_form})