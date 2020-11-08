# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ChannelSerializer, MessageSerializer
from .models import Channel, Message


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Channels to be viewed
    """
    queryset = Channel.objects.filter(visible=True).order_by('name')
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Messages to be viewed.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of the latest 50 messages sent in a
        channel
        """
        channel = Channel.objects.get(pk=self.request.GET['channel'])
        return Message.objects.filter(
            channel=channel
        ).order_by("-timestamp")[:50]
