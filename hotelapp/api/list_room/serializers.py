from hotelapp.models import Room
from rest_framework.serializers import ModelSerializer

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomViewSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','title','description','images','price','type','status']