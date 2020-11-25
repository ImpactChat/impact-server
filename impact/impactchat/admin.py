from django.contrib import admin
from .models import Channel
# Register your models here.


@admin.register(Channel)
class AuthorAdmin(admin.ModelAdmin):
    pass
