from channels.generic.websocket import AsyncJsonWebsocketConsumer
from djangochannelsrestframework import permissions
from channels.consumer import AsyncConsumer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin, )
from typing import Dict, Any
import jwt
from django.conf import settings

from .models import Channel
from impactadmin.models import User
from .serializers import ChannelSerializer
from impactadmin.serializers import UserSerializer


class EchoConsumer(AsyncJsonWebsocketConsumer):
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


class TokenAuth(permissions.BasePermission):
    async def has_permission(self, scope: Dict[str,
                                               Any], consumer: AsyncConsumer,
                             action: str, **kwargs) -> bool:
        token = kwargs['data']['token']
        print("Token:", token)
        try:
            print("Decoded:",
                  jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256']))
        except jwt.exceptions.ExpiredSignatureError:
            print("Expired")
            return False
        return True


class ChannelConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = (TokenAuth, )


class UserConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )
