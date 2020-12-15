from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from djmoney.settings import CURRENCY_CHOICES

from .serializers import UserSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # return current user
    def get_object(self):
        user = self.request.user
        return user


class AllCurrencuesView(APIView):
    """
    A view that returns list of available currencies.
    """

    def get(self, request, format=None):
        content = [{'code': code, 'name': name} for code, name in CURRENCY_CHOICES]
        return Response(content)
