from rest_framework import serializers

from .models import Managers


class ManagerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField()
    full_name = serializers.CharField(write_only=True)

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

        user = Managers.objects.create_user(**validated_data)
        user.full_name = full_name
        user.save()

        return user


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Managers
        fields = ['full_name', 'phone', 'email', ]
