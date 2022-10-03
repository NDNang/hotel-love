from hotelapp.models import TypeBook
from rest_framework.serializers import ModelSerializer

class TypeBookSerializer(ModelSerializer):
    class Meta:
        model = TypeBook
        fields = '__all__'