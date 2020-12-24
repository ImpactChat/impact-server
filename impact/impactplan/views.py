from rest_framework import viewsets
from .models import Classe
from .serializers import CodeSerializer
from rest_framework import permissions


# Create your views here.
class ClasseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Channels to be viewed
    """
    queryset = Classe.objects.filter(posted=True).order_by('name')
    serializer_class = CodeSerializer
    permission_classes = [permissions.IsAuthenticated]
