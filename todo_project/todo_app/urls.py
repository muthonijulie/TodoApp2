from django.urls import path
from .views import hello,index,task_list,task_detail,task_create,task_update,task_delete
urlpatterns=[
    path('hello',hello),
    path('index/',index,name='index'),
    path('',task_list,name='list'),
    path('detail/<int:id>/',task_detail,name='detail'),
    path('create/',task_create,name='create'),
    path('update/<int:id>/',task_update,name='update'),
    path('delete/<int:id>/',task_delete,name='delete'),
]