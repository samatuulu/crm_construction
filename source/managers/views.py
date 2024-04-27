from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Managers
from .serializers import ManagerRegistrationSerializer


class ManagerRegistrationAPIView(generics.CreateAPIView):
    queryset = Managers.objects.all()
    serializer_class = ManagerRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        manager = serializer.instance
        refresh = RefreshToken.for_user(manager)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class ManagerLoginAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({
                "detail": "Invalid credentials"
            }, status=status.HTTP_401_UNAUTHORIZED)


class ManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = Managers.objects.all()
    serializer_class = ManagerRegistrationSerializer
    permission_classes = [IsAuthenticated]


class ManagerDeleteAPIView(generics.DestroyAPIView):
    queryset = Managers.objects.all()
    permission_classes = [IsAuthenticated]
