from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f'room_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

        # async_to_sync(self.channel_layer.group_send)(
        #     f'room_{self.room_name}',
        #     {
        #         'value': json.dumps({'status': 'online'})
        #     }
        # )

        data = {'type': 'connected'}
        self.send(text_data=json.dumps(
            {
                'payload':'connected'
            }
        ))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        payload={'message':data.get('message'),'sender':data.get('sender')}

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            f'room_{self.room_name}',
            {
                'type': 'send_message',
                'value': json.dumps(payload)
            }
        )

    # Receive message from room group
    def send_message(self, text_data):
        data = json.loads(text_data.get('value'))
        # self.send(text_data=json.dumps(data))
        self.send(text_data=json.dumps(
            {
                'payload':data
            }
        ))