from django.conf.urls import url
from django.urls import path
from rango import views

app_name= 'rango'

urlpatterns =[
    url('', views.index, name='index'),
]

dodo :P
