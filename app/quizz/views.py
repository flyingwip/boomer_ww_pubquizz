# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import viewsets, mixins, status
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Quizz


from quizz import serializers


class BaseViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset.filter(
    #         user=self.request.user
    #     ).order_by('-name').distinct()


class QuizzViewSet(BaseViewSet):
    """Manage quizzes in database"""
    queryset = Quizz.objects.all()
    serializer_class = serializers.QuizzSerializer
