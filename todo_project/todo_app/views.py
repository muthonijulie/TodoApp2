from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms import TaskCreateForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.

def task_list(request):
    tasks= Task.objects.all()
    paginator=Paginator(tasks,4,orphans=4,allow_empty_first_page=True)

    page=request.GET.get('page')

    try:
        paginated_tasks=paginator.page(page)
    except PageNotAnInteger:
        paginated_tasks=paginator.page(1)
    except EmptyPage:
        paginated_tasks=paginated_tasks.page(paginator.num_pages)
    
    title='List'
    return render(request,'todo_app/list.html',{'tasks':paginated_tasks,'title':title})

   
def task_detail(request,id):
    task=get_object_or_404(Task,id=id)
    #print(task)
    title='Detail'
    return render(request,'todo_app/detail.html',{'task':task,'title':title})

@login_required
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
@login_required
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
@login_required
def task_delete(request,id):
    task=get_object_or_404(Task, id=id)
    if request.method=='POST':
        task.delete()
        return redirect('list')
    title='Delete'
    
    return render(request,'todo_app/delete.html',{'task':task,'title':title})