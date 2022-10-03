from hotelapp.models import FreeServiceRoom
from rest_framework.serializers import ModelSerializer

class FreeServiceRoomSerializer(ModelSerializer):
    class Meta:
        model = FreeServiceRoom
        fields = '__all__'