from rest_framework import serializers
from .models import MasterPlayer

class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterPlayer
        fields='__all__'