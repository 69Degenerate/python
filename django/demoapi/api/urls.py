
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.front),
    path('r',views.read),
    path('w',views.write),
    path('s/<str:c>/<str:val>',views.search)
]
