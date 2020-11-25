from django.urls import re_path

from .multiplexer import Demultiplexer
from .consumers import ChannelConsumer

websocket_urlpatterns = [
    re_path(r'^ws/$', Demultiplexer.as_asgi()),
]
