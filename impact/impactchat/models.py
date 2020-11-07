from django.conf import settings
from django.db import models


class Channel(models.Model):
    """
    Represents a chat channel. If ``visible`` is set to ``False``, the channel
    shouldn't be included in a list of channels. This is prefered as it
    conserves the messages in the database as opposed to simply deleting the
    channel.
    """
    class Meta:
        permissions = [
            ("manage_channels", "Can manage channels"),
        ]

    name = models.CharField(max_length=32,
                            unique=True,
                            verbose_name="Channel name",
                            help_text="Name of the channel")
    visible = models.BooleanField(
        default=True,
        help_text="Whether the channel should be visible to normal users")

    def __str__(self):
        return self.name


class Message(models.Model):
    """
    Represent a chat message
    """
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        help_text="Key to the channel in which the message was posted")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="key to the user model that created the message")

    content = models.CharField(
        max_length=2000,
        help_text="Content of the message, limited to 2 000 characters.")
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime at which the message was created, defaults to now")

    def __str__(self):
        return f"{self.author}:{self.channel.name}/{self.pk}"
