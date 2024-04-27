from rest_framework import generics

from .serializers import ApartmentSerializer, ClientSerializer
from .models import Apartment, Client


class ApartmentAPIView(generics.CreateAPIView):
    serializer_class = ApartmentSerializer


class ApartmentListAPIView(generics.ListAPIView):
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        if status in ['active', 'reserved', 'sold', 'installment', 'barter']:
            queryset = Apartment.objects.filter(status=status)
        else:
            queryset = Apartment.objects.all()
        return queryset


class ApartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ClientAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
