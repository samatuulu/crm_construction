from django.urls import path

from .views import ManagerRegistrationAPIView, ManagerUpdateAPIView, ManagerDeleteAPIView, ManagerLoginAPIView

urlpatterns = [
    path('register/', ManagerRegistrationAPIView.as_view(), name='manager_register'),
    path('login/', ManagerLoginAPIView.as_view(), name='manager_login_url'),
    path('update/<int:pk>/', ManagerUpdateAPIView.as_view(), name='manager_update'),
    path('delete/<int:pk>/', ManagerDeleteAPIView.as_view(), name='manager_delete'),

]
