from channels.generic.websocket import AsyncJsonWebsocketConsumer
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
)

from .models import Channel
from impactadmin.models import User
from .serializers import ChannelSerializer
from impactadmin.serializers import UserSerializer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room groups
        pass

    # Receive message from WebSocket
    async def receive_json(self, data):
        print(data)
        self.send_json({
            "type": "websocket.send",
            "text": data,
        })


class ChannelConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = (permissions.AllowAny,)


class UserConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
