from hotelapp.models import ListCode
from rest_framework.serializers import ModelSerializer

class CodeSerializer(ModelSerializer):
    class Meta:
        model = ListCode
        fields = '__all__'