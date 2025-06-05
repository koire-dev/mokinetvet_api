from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from permissions import IsAdmin, IsOwnerOrAdmin
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    MyTokenObtainPairSerializer
)

User = get_user_model()


from django.http import JsonResponse

def home_view(request):
    return JsonResponse({'message': 'Bienvenue sur l’API MOKINEVET'})


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = UserSerializer
    lookup_field = 'pk'


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.is_active = False
        request.user.save()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

