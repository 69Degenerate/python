import datetime

from django.db.models import Subquery, Count
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from service.serializers.order_point_serializer import Order_point_serializer
from service.serializers.order_content_serializer import Order_content_serializer
from service.serializers.order_modifer_serializer import Order_modifer_serializer
from service.serializers.order_serializer import Order_serializer
from service.serializers.content_assign_serializer import Content_assign_serializer
from service.serializers.user_settings_serializer import UserSettingReaderSerializer
from service.serializers.stations_serializer import Stations_serializer, StationsReadSerializer
from service.serializers.staff_serializer import StaffReaderSerializer, StaffWriterSerializer
from .models import Order_point, Order, Order_content, Order_modifer, Stations, Staff, UserSettings, OrderStatusName,Content_assign
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import string
import random
from django.db.models import Q
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from datetime import datetime
import json
from django.core import serializers


# import datetime

# Create your views here.
@api_view(['GET', 'POST'])
def orderPoint(request):
    order_points = Order_point.objects.all()
    serializer = Order_point_serializer(order_points, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def orderList(request):
    result = {}
    orderList = Order.objects.all()
    serializers = Order_serializer(orderList, many=True)
    result["order"] = serializers.data
    for orderIndex, order in enumerate(orderList, start=0):
        print(order.id)
        orderContent = Order_content.objects.filter(orderId=order.id)
        contentSerializers = Order_content_serializer(orderContent, many=True)
        print(orderIndex)
        result["order"][orderIndex]["Appetizer"] = contentSerializers.data
        print(orderContent)
        for modifierIndex, modifier in enumerate(orderContent, start=0):
            modifierContent = Order_modifer.objects.filter(contentID=modifier.id)
            modifier_serializer = Order_modifer_serializer(modifierContent, many=True)
            result["order"][orderIndex]["Appetizer"][modifierIndex]["subItems"] = modifier_serializer.data
            print(modifierContent)
    print(result)
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def PostOrder(request):
    print(request.method)
    orderData = JSONParser().parse(request)
    serializers = Order_serializer(data=orderData)
    if serializers.is_valid():
        serializers.save()
        return JsonResponse(serializers.data, status=status.HTTP_201_CREATED)
    print(serializers)
    return JsonResponse({'message': 'something went wrong please check your response'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
class TestingViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializers = Order_serializer
    # return 

class StationsView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        stationList = Stations.objects.filter(isStation=True).all()
        serializers = StationsReadSerializer(stationList, many=True)
        return JsonResponse(serializers.data, safe=False)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('stationName'),
            'station_name': request.data.get('stationName'),
            'colorCode': request.data.get('colorCode'),
            'client_id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            'client_secrete': ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            'tag': '1',
            'isStation': request.data.get('isStation'),
        }
        print(data)
        serializer = Stations_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StationsDetailView(APIView):

    def get_object(self, stationId):
        try:
            return Stations.objects.get(id=stationId)
        except Stations.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, stationId, *args, **kwargs):
        station_instance = self.get_object(stationId)
        if not station_instance:
            return Response(
                {"res": "Station with  id " + str(stationId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StationsReadSerializer(station_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, stationId, *args, **kwargs):
        station_instance = self.get_object(stationId)
        if not station_instance:
            return Response(
                {"res": "Station with id " + str(stationId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'station_name': request.data.get('stationName'),
            'colorCode': request.data.get('colorCode'),
        }
        serializer = Stations_serializer(instance=station_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, stationId, *args, **kwargs):
        station_instance = self.get_object(stationId)
        if not station_instance:
            return Response(
                {"res": "Station with id " + str(stationId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        station_name = station_instance.station_name;
        station_instance.delete()
        return Response(
            {"res": station_name + " deleted!"},
            status=status.HTTP_200_OK
        )


class StaffView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        stationList = Staff.objects.all()
        serializers = StaffReaderSerializer(stationList, many=True)
        return JsonResponse(serializers.data, safe=False)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('firstName'),
            'last_name': request.data.get('lastName'),
            'staff_type': 1,
            'active_status': 1,
            'station_id': None,
        }
        print(data)
        serializer = StaffWriterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffDetailView(APIView):

    def get_object(self, staffId):
        try:
            return Staff.objects.get(id=staffId)
        except Staff.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, staffId, *args, **kwargs):
        staff_instance = self.get_object(staffId)
        if not staff_instance:
            return Response(
                {"res": "Staff with  id " + str(staffId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StaffReaderSerializer(staff_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, staffId, *args, **kwargs):
        staff_instance = self.get_object(staffId)
        if not staff_instance:
            return Response(
                {"res": "Staff with id " + str(staffId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
        }
        if request.data.get('firstName'):
            data['first_name'] = request.data.get('firstName')
        if request.data.get('lastName'):
            data['last_name'] = request.data.get('lastName')
        if request.data.get('staffType'):
            data['staff_type'] = request.data.get('staffType')
        if request.data.get('activeStatus'):
            data['active_status'] = request.data.get('activeStatus')
        if request.data.get('stationId'):
            data['station_id'] = request.data.get('stationId')
            selectedStation = StationsDetailView.get_object(StationsDetailView, request.data.get('stationId'))
            if not selectedStation:
                return Response(
                    {"res": "Station with  id " + str(request.data.get('stationId')) + " does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            print(selectedStation)

        serializer = StaffWriterSerializer(instance=staff_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, staffId, *args, **kwargs):
        staff_instance = self.get_object(staffId)
        if not staff_instance:
            return Response(
                {"res": "Staff with id " + str(staffId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        staffName = staff_instance.last_name
        staff_instance.delete()
        return Response(
            {"res": staffName + " deleted!"},
            status=status.HTTP_200_OK
        )


class StationsStaffView(APIView):

    def get(self, request, stationId, *args, **kwargs):
        stationList = Staff.objects.filter(station_id=stationId).all()
        serializers = StaffReaderSerializer(stationList, many=True)
        return JsonResponse(serializers.data, safe=False)


class UserSettingsView(APIView):

    def get_object(self, stationId):
        try:
            return UserSettings.objects.get(stationId=stationId)
        except UserSettings.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, stationId, *args, **kwargs):
        user_settings = self.get_object(stationId)
        if not user_settings:
            return Response(
                {"res": "User Settings not found for id " + str(stationId)},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSettingReaderSerializer(user_settings)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. Delete
    def delete(self, request, stationId, *args, **kwargs):
        user_settings = self.get_object(stationId)
        if not user_settings:
            return Response(
                {"res": "User Settings not found for id " + str(stationId)},
                status=status.HTTP_400_BAD_REQUEST
            )
        user_settings.delete()
        return Response(
            {"res": " deleted!"},
            status=status.HTTP_200_OK
        )

    def post(self, request, stationId, *args, **kwargs):
        ### check station settings available or not
        station_instance = StationsDetailView.get_object(self, stationId)
        if not station_instance:
            return Response(
                {"res": "Station with  id " + str(stationId) + " does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'notification': request.data.get('notification'),
            'cooking': request.data.get('cooking'),
            'incoming': request.data.get('cooking'),
            'dragged': request.data.get('cooking'),
            'complete': request.data.get('cooking'),
            'cancel': request.data.get('cooking'),
            'recall': request.data.get('cooking'),
            'priority': request.data.get('cooking'),
            'nearTo': request.data.get('cooking'),
            'stationId': stationId
        }
        user_settings = self.get_object(stationId)

        serializer = UserSettingReaderSerializer(instance=user_settings, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def stationOrder(request):
    requestJson = JSONParser().parse(request)
    start = requestJson.get('start')
    end = requestJson.get('end')
    all_orders = Order.objects.filter(arrival_time__date__gte=start, arrival_time__date__lte=end).values_list("id")
    stationList = Stations.objects.filter(isStation=True).all()
    response = []
    for station in stationList:
        test = Order_content.objects.filter(
            orderId__in=all_orders,
            stationId=station.id
        )
        print(test)
        station_details = {
            "id": station.id,
            "name": station.station_name,
            "count": len(test),
            "colorCode": station.color_code
        }
        response.append(station_details)
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def orderCount(request):
    requestJson = JSONParser().parse(request)
    start = requestJson.get('start')
    end = requestJson.get('end')
    order_status = OrderStatusName.objects.all()
    # order = Order.objects.filter(arrival_time__date__gte=start, arrival_time__date__lte=end).values(
    #     'order_status').annotate(Count=Count('order_status'))
    # print(order)
    response = []
    for orderStatus in order_status:
        data = {
            "status": orderStatus.id,
            "name": orderStatus.orderName,
            "count": len(Order.objects.filter(order_status=orderStatus.id, arrival_time__date__gte=start,
                                              arrival_time__date__lte=end).values('order_status').annotate(
                Count=Count('order_status')).values_list())
        }
        response.append(data)

    return Response(response, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def ticketSearch(request):
#     requestJson = JSONParser().parse(request)
#     ticketId = requestJson.get('ticketId')
#     tableId = requestJson.get('tableId')

#     if ticketId is not None:
#         print(ticketId)
#         try:
#             orders = Order.objects.filter(Q(externalOrderId=ticketId) | Q(id=ticketId))
#             serializedData = Order_serializer(orders, many=True)
#         except:
#             return Response({"error": "Invalid ticket Id"}, status=status.HTTP_400_BAD_REQUEST)
#     elif tableId is not None:
#         print(tableId)
#     else:
#         print("invalid arguments")
#         return Response({"error": "invalid arguments"}, status=status.HTTP_400_BAD_REQUEST)
#     return Response(serializedData.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ticketSearch(request,ticketId):
    result = {}
    date=datetime.datetime.today().strftime("%d/%m/20%y")
    print(type(date))
    od=Order.objects.values_list('arrival_time', flat=True).get(pk=ticketId)
    orderList = Order.objects.filter((Q(externalOrderId=ticketId) | Q(id=ticketId)) & Q(arrival_time__contains=date))
    # orderList = Order.objects.filter(Q(externalOrderId=ticketId) | Q(id=ticketId))
    serializers = Order_serializer(orderList, many=True)
    result["order"] = serializers.data
    for orderIndex, order in enumerate(orderList, start=0):
        orderContent = Order_content.objects.filter(Q(orderId=order.id) | Q(orderId=order.externalOrderId))
        contentSerializers = Order_content_serializer(orderContent, many=True)
        result["order"][orderIndex]["Appetizer"] = contentSerializers.data      
        for modifierIndex, modifier in enumerate(orderContent, start=0):
            modifierContent = Order_modifer.objects.filter(contentID=modifier.id)
            modifier_serializer = Order_modifer_serializer(modifierContent, many=True)
            result["order"][orderIndex]["Appetizer"][modifierIndex]["subItems"] = modifier_serializer.data
        for caIndex, ca in enumerate(orderContent, start=0):         
            contentassign =Content_assign.objects.filter(contentID=ca.id)
            ca_serializer = Content_assign_serializer(contentassign, many=True)
            result["order"][orderIndex]["Appetizer"][caIndex]["AssignedTo"] = ca_serializer.data
    return JsonResponse(result, safe=False)
    # return Response(serializers.data)
    
@api_view(['POST'])
def ticketInsert(request, room_name):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_name,
        {
            'type': 'chat_message',
            'message': request,
            'username': 'testal',
            'date': ''
        }
    )
    return Response({"status": "inserted"}, status=status.HTTP_200_OK)

