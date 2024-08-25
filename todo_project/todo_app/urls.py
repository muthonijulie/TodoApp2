from django.urls import path
from .views import hello,index
urlpatterns=[
    path('',hello),
    path('index/',index,name='index')
]