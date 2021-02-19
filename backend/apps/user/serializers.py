from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'main_currency')
