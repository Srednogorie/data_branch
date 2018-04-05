from rest_framework import serializers
from data_core.models import AubsaigTrend


class AubsaigTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = AubsaigTrend
        fields = ('period', 'manufacturing', 'services', 'construction')
