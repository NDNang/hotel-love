from rest_framework.serializers import ModelSerializer,ReadOnlyField,CharField,ListField
from hotelapp.models import BookRoom


class BookRoomSerializer(ModelSerializer):
    fullname = CharField(source='customer.fullname')
    phone = CharField(source='customer.phone')
    room_name = CharField(allow_blank=True, allow_null=True,source='room.name')
    code_name = CharField(allow_blank=True, allow_null=True,source='code_pay.name')
    class Meta:
        model = BookRoom
        fields = '__all__'

class BookRoomStatusSerializer(ModelSerializer):
    class Meta:
        model = BookRoom
        fields = ['id','is_pay','status']

