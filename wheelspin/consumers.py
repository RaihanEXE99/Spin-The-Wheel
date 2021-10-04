
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

class WheelRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'room_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        room_name = text_data_json['room_name']
        activeCouter = text_data_json['activeCouter']

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'room_name': room_name,
                'activeCouter': activeCouter,
            }
        )

    async def chatroom_message(self, event):
        room_name = event['room_name']
        activeCouter = event['activeCouter']

        await self.send(text_data=json.dumps({
            'room_name': room_name,
            'activeCouter': activeCouter,
        }))
    pass

