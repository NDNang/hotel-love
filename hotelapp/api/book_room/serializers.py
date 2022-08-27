from rest_framework.serializers import ModelSerializer,ReadOnlyField,CharField,ListField
from hotelapp.models import BookRoom,ServiceRoom,ExtraService


class BookRoomSerializer(ModelSerializer):
    fullname = CharField(source="customer.fullname")
    phone = CharField(source="customer.phone")
    room_name = ReadOnlyField(source="room.name")
    class Meta:
        model = BookRoom
        fields = ['id','fullname','phone','room_name','date','time_in','time_out','status','room_id','customer_id']
