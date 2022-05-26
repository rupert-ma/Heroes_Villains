from rest_framework import serializers
from .models import Super, SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type', 'super']
        depth = 1