from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms import TaskCreateForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from django.views.generic import View,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
# Create your views here.
class TaskListView(View):
   template_name='todo_app/list.html' 
   

   def get(self,request):
    tasks= Task.objects.all()
    paginator=Paginator(tasks,3,orphans=4,allow_empty_first_page=True)

    page=request.GET.get('page')

    try:
        paginated_tasks=paginator.page(page)
    except PageNotAnInteger:
        paginated_tasks=paginator.page(1)
    except EmptyPage:
        paginated_tasks=paginated_tasks.page(paginator.num_pages)
    
    title='List'
    context={'tasks':paginated_tasks,'title':title}
    return render(request,self.template_name,context)

class TaskDetailView(DetailView):
    model=Task
    template_name='todo_app/detail.html'
    context_object_name='task'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Task'
        return context
    # task=get_object_or_404(Task,id=id)
    # #print(task)
    # title='Detail'
    # return render(request,'todo_app/detail.html',{'task':task,'title':title})

# @login_required
class TaskCreateView(LoginRequiredMixin,CreateView):
    model=Task
    form=TaskCreateForm
    fields=['title','description','status','due_date','author']
    template_name='todo_app/create.html'
    success_url='/'

    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        context['title']='Create '
        return context

# def task_create(request):
#     if request.method == 'POST':
#         form=TaskCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#     else:
#             form=TaskCreateForm()
#             title='Create'
#     return render(request,'todo_app/create.html',{'form':form,'title':title})
# @login_required
@method_decorator(login_required,name='dispatch')
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Task
    form=TaskCreateForm
    fields=['title','description','status','due_date','author']
    template_name='todo_app/update.html'
    success_url='/'

    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        context['title']='Update '
        return context

# def task_update(request,id):
#      task=get_object_or_404(Task,id=id)
#      if request.method=='POST':
#           form=TaskCreateForm(request.POST or None,instance=task)
#           if form.is_valid():
#            form.save()
#            return redirect('list')
#      else:
#           form=TaskCreateForm(instance=task)
#           title='Update'

#      return render(request,'todo_app/update.html',{'form':form,'title':title,'task':task})
 
# @login_required
# def task_delete(request,id):
#     task=get_object_or_404(Task, id=id)
#     if request.method=='POST':
#         task.delete()
#         return redirect('list')
#     title='Delete'
    
#     return render(request,'todo_app/delete.html',{'task':task,'title':title,'task':task})
@method_decorator(login_required,name='dispatch')
class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    form=TaskCreateForm
    fields=['title','description','status','due_date','author']
    template_name='todo_app/delete.html'
    success_url='/'

    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        context['title']='Delete '
        return context
