from django.urls import path
from .views import ApartmentAPIView, ApartmentRetrieveUpdateDestroyAPIView, ApartmentListAPIView,\
    ClientAPIView, ClientRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('create/', ApartmentAPIView.as_view(), name='apartment_create'),
    path('update/<int:pk>/', ApartmentRetrieveUpdateDestroyAPIView.as_view(), name='apartment_update'),
    path('apartments/', ApartmentListAPIView.as_view(), name='apartment_list'),

    path('client/create/', ClientAPIView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_update'),

]
