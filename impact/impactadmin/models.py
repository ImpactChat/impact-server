from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model, adds the ``avatar`` and ``locale`` fields
    """
    avatar = models.CharField(max_length=1,
                              default="U",
                              help_text="Avatar of the user")
    locale = models.CharField(max_length=2,
                              default="en",
                              choices=settings.LANGUAGES,
                              help_text="Which language does the user use")
