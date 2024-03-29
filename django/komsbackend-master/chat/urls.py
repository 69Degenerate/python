from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('ticketInsert/<str:room_name>/<str:user_name>', views.ticketInsert, name='ticketInsert'),
]
