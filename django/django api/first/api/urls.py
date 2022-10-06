
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users',views.users,name='users'),
    path('newuser',views.newuser,name='newuser'),
    path('',views.read,name='read'),
    path('readall',views.readall,name='readall'),
    path('read/<str:pk>',views.read2,name='read2'),
    path('create',views.create,name='create'),
    path('add',views.add,name='add'),
    path('update/',views.update,name='update'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
]
