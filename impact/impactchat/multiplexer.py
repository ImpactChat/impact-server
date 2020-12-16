from .consumers import UserConsumer, ChannelConsumer

from channels_demultiplexer.demultiplexer import WebsocketDemultiplexer


class Demultiplexer(WebsocketDemultiplexer):
    # Wire your async JSON consumers here: {stream_name: consumer}
    consumer_classes = {
        "channel": ChannelConsumer,
        "user": UserConsumer,
    }
