from rest_framework import generics

from .serializers import ManagerRegistrationSerializer, ManagerSerializer
from .models import Managers


class ManagerRegistrationAPIView(generics.CreateAPIView):
    serializer_class = ManagerRegistrationSerializer


class ManagerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Managers.objects.all()
    serializer_class = ManagerSerializer
