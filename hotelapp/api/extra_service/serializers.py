from rest_framework.serializers import ModelSerializer
from hotelapp.models import ExtraService


class ExtraServiceSerializer(ModelSerializer):
    class Meta:
        model = ExtraService
        fields = '__all__'

