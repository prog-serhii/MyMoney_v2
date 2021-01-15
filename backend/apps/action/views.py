from datetime import date

from rest_framework.generics import ListAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import ActionSerializer
from .models import Action


class SmallResultSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10


class ActionListView(ListAPIView):
    serializer_class = ActionSerializer
    pagination_class = SmallResultSetPagination
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name', )
    ordering_fields = ('date', 'name')
    lookup_fields = ('wallet', )

    def get_queryset(self):
        queryset = Action.objects.all()

        # from_date = self.request.query_params.get('from', None)
        # to_date = self.request.query_params.get('to', None)

        # if from_date is not None:
        #     try:
        #         from_date = date.fromisoformat(from_date)
        #     except ValueError as e:
        #         print(str(e))

        # if to_date is not None:
        #     try:
        #         to_date = date.fromisoformat(to_date)
        #     except ValueError as e:
        #         print(str(e))

        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):
                filter[field] = self.kwargs[field]
        return Action.objects.filter(**filter)
