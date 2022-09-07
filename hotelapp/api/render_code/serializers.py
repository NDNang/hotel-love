from hotelapp.models import Code
from rest_framework.serializers import ModelSerializer

class CodeSerializer(ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'