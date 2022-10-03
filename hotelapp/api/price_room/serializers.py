from hotelapp.models import PriceRoom
from rest_framework.serializers import ModelSerializer

class PriceRoomSerializer(ModelSerializer):
    class Meta:
        model = PriceRoom
        fields = '__all__'