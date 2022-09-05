from rest_framework.serializers import ModelSerializer,ReadOnlyField,CharField,PrimaryKeyRelatedField
from hotelapp.models import BookRoom

class BookRoomSerializer(ModelSerializer):
    class Meta:
        model = BookRoom
        fields = '__all__'
