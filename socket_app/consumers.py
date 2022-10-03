import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AdminConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'alert_data'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data_json = json.loads(text_data)
        # message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'alert_data',
                'message': data_json
            }
        )

    # Receive message from room group
    async def alert_data(self, data):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type':'data_book_room',
            'message': data
        }))
