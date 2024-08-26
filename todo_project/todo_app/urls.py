from django.urls import path
from .views import hello,index,task_list,task_detail
urlpatterns=[
    path('hello',hello),
    path('index/',index,name='index'),
    path('',task_list,name='list'),
    path('detail/<int:id>/',task_detail,name='detail'),
]