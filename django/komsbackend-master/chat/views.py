from django.shortcuts import render
from rest_framework.decorators import api_view
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
import json
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

@api_view(['POST'])
def ticketInsert(request, room_name, user_name):
    requestJson = JSONParser().parse(request)
    channel_layer = get_channel_layer()
    data = async_to_sync(channel_layer.group_send)(
        'chat_%s' % room_name,
        {
            'type': 'chat_message',
            'message': json.dumps(requestJson),
            'username': user_name
        }
    )
    print(data)
    return Response({"status": "inserted"}, status=status.HTTP_200_OK)