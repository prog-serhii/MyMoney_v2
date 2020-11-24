from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer


class SignUpView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
