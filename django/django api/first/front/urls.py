
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('view',views.view,name='view'),
    path('add',views.add,name='add'),
    path('update',views.update,name='update'),
    path('update1/<int:id>',views.update1,name='update1'),
    path('update1/',views.update1,name='update1'),
    path('delete',views.delete,name='delete'),
    path('delete/<int:id>',views.delete,name='delete1'),

]
