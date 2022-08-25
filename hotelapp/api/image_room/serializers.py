from hotelapp.models import ImageRoom
from rest_framework.serializers import ModelSerializer

class ImageRoomSerializer(ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = '__all__'