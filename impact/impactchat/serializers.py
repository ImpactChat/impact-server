from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Channel, Message


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['name', 'pk']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'avatar', 'locale', 'pk']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.CharField(max_length=2000)
    author = UserSerializer()
    timestamp = serializers.DateTimeField()
    pk = serializers.IntegerField()

    class Meta:
        model = Message
        fields = ['content', 'author', 'timestamp', 'pk']
