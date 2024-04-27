from django.urls import path
from .views import ManagerRegistrationAPIView, ManagerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register/', ManagerRegistrationAPIView.as_view(), name='manager_register'),
    path('update/<int:pk>/', ManagerRetrieveUpdateDestroyAPIView.as_view(), name='manager_update'),

]
