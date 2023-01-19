
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.front),
    path('r',views.read),
    path('w',views.write),
    # path('w/<int:pk>',views.update),
    path('s/<str:c>/<str:val>',views.search),
    path('d/<int:pk>',views.delete),
    path('ad/<int:pk>',views.apidel),
    path('u/<int:pk>',views.update),
]
