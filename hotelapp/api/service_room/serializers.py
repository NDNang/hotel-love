from rest_framework.serializers import ModelSerializer
from hotelapp.models import ServiceRoom


class ServiceRoomSerializer(ModelSerializer):
    class Meta:
        model = ServiceRoom
        fields = '__all__'

