from rest_framework import serializers
from .models import Classe


class CodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classe
        fields = [
            'name',
            'classe_groupe',
            'prof',
            'start',
            'end',
            'code',
            'link',
            'posted',
            'pk'
        ]
