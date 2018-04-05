from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import AubsaigTrend
from ..serializers import AubsaigTrendSerializer


class AustraliaAigTrend(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = AubsaigTrend.objects.all()
    serializer_class = AubsaigTrendSerializer
