from rest_framework import serializers
from . models import customer

class customerSerializers(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields='__all__'

