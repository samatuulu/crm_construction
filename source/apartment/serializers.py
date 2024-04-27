from rest_framework import serializers

from .models import Apartment, Client


class ApartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apartment
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
