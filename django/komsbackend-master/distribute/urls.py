from django.urls import path
from service import views

#register your controller

urlpatterns = [

    path('OrderList/', views.orderList, name='orderPoints'),

]