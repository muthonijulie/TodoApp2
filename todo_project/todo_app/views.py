from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello there.This our basic todo app</h1>")

def index(request):
    context={
        'name':'Muthoni Julius'
    }
    return render(request,'todo_app/index.html',context)

