from djoser.serializers import UserCreateSerializer, UserSerializer

from django.contrib.auth import get_user_model

from apps.core.validators import CurrencyCodeValidator


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password')


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'name', 'main_currency')
