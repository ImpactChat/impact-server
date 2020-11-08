from django.urls import include, path
from rest_framework import routers
from .views import ChannelViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'messages', MessageViewSet, basename='Message')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
