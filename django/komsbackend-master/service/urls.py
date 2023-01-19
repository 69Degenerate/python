from django.urls import path
from service import views
from django.urls import path
from django.contrib import admin
#register your controller

urlpatterns = [
    path('OrderList/', views.orderList, name='orderPoints'),
    path('TestingViewSet/', views.TestingViewSet, name="TestingViewSet"),
    # path("PostOrder/", views.PostOrder, name="PostOrder"),
    # path("getStations/",views.getStation,name="getStations"),
    # path("addStations/",views.addStation,name="addStations"),
    # path("updateStations/<int:stationId>", views.updateStation, name="updateStations"),
    # path("deleteStations/", views.deleteStation, name="deleteStations"),
    path('station', views.StationsView.as_view()),
    path('station/<int:stationId>/', views.StationsDetailView.as_view()),
    path('staff', views.StaffView.as_view()),
    path('staff/<int:staffId>/', views.StaffDetailView.as_view()),
    path('stationWiseStaff/<int:stationId>/', views.StationsStaffView.as_view()),
    path('userSettings/<int:stationId>/', views.UserSettingsView.as_view()),
    path('stationOrder/', views.stationOrder, name='stationOrder'),
    path('orderStatus/', views.orderCount, name='orderStatus'),
    path('orderSearch/<ticketId>', views.ticketSearch, name='orderSearch'),
 
    
    # path('ticketInsert/<str:room_name>/', views.ticketInsert, name='ticketInsert'),
    # path('/UpdateOrderStatus', , name='pending_processing_ready_onHold_Cancel,recall'),
    # path('/UpdateOrderContentStatus', , name=''),
    # path('/OrderList',,name='')
]