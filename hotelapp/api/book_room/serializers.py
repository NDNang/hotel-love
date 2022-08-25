from rest_framework.serializers import ModelSerializer
from hotelapp.models import BookRoom


class BookRoomSerializer(ModelSerializer):
    class Meta:
        model = BookRoom
        fields = '__all__'

