from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

from .models import Managers


class ManagerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Managers
        fields = ['full_name', 'phone', 'email', 'password']

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        first_name, *last_name = full_name.split()
        validated_data['first_name'] = first_name
        validated_data['last_name'] = ' '.join(last_name) if last_name else ''

        username = validated_data['email'].split('@')[0]
        validated_data['username'] = username

        if Managers.objects.filter(username=username).exists():
            raise ValidationError("Username already exists. Please update your email.")

        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)

        manager = super().create(validated_data)
        manager.full_name = full_name
        manager.save()
        return manager

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Managers
        fields = ['full_name', 'phone', 'email', ]
