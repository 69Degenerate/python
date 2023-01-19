import json
import logging
import random
from datetime import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from message.models import Message


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("connect")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        print("disconnect")
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print("Receive")
        print("receive room_name : "+str(self.room_name)+" , group_name : "+str(self.room_group_name)+", channel : "+str(self.channel_name))
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
                'date': str(datetime.now().strftime("%Y-%m-%d %H:%M"))
            }
        )
        Message.objects.create(body=message, sender=self.user)

    # Receive message from room group
    def chat_message(self, event, type='chat_message'):
        print("Chat Message")
        message = event['message']
        username = event['username']

        # Send message to WebSocket

        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'username': username,
        }))
