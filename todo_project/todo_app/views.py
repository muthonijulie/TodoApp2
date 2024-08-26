from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskCreateForm

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello there.This our basic todo app</h1>")

def index(request):
    context={
        'name':'Muthoni Julius'
    }
    return render(request,'todo_app/index.html',context)

def task_list(request):
    tasks= Task.objects.all()
    return render(request,'todo_app/list.html',{'tasks':tasks})

def task_detail(request,id):
    task=get_object_or_404(Task,id=id)
    return render(request,'todo_app/detail.html',{'task':task})

def task_create(request):
    if request.method == 'POST':
        form=TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
            form=TaskCreateForm()
    return render(request,'todo_app/create.html',{'form':form})


