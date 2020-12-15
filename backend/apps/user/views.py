from rest_framework import generics

from .serializers import UserSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # return current user
    def get_object(self):
        user = self.request.user
        return user
