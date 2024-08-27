from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms import TaskCreateForm
# Create your views here.

def task_list(request):
    tasks= Task.objects.all()
    title='List'
    return render(request,'todo_app/list.html',{'tasks':tasks,'title':title})

   
def task_detail(request,id):
    task=get_object_or_404(Task,id=id)
    title='Detail'
    return render(request,'todo_app/detail.html',{'task':task,'title':title})


def task_create(request):
    if request.method == 'POST':
        form=TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
            form=TaskCreateForm()
            title='Create'
    return render(request,'todo_app/create.html',{'form':form,'title':title})

def task_update(request,id):
     task=get_object_or_404(Task,id=id)
     if request.method=='POST':
          form=TaskCreateForm(request.POST,instance=task)
          if form.is_valid():
           form.save()
           return redirect('list')
     else:
          form=TaskCreateForm(instance=task)
          title='Update'

     return render(request,'todo_app/update.html',{'form':form,'title':title})

def task_delete(request,id):
    task=get_object_or_404(Task, id=id)
    if request.method=='POST':
        task.delete()
        return redirect('list')
    title='Delete'
    
    return render(request,'todo_app/delete.html',{'task':task,'title':title})