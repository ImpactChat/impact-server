from django.urls import include, path
from rest_framework import routers
from .views import ClasseViewSet

router = routers.DefaultRouter()
router.register(r'codes', ClasseViewSet, basename='Classe')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
