from rest_framework import viewsets
from .models import Classe
from .serializers import CodeSerializer
from rest_framework import permissions


# Create your views here.
class ClasseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Channels to be viewed
    """
    queryset = Classe.objects.filter(posted=True).order_by('start')
    serializer_class = CodeSerializer
    # Probably should change this but its bugged so...
    permission_classes = [permissions.AllowAny]
