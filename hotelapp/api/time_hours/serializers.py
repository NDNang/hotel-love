from hotelapp.models import TimeHours
from rest_framework.serializers import ModelSerializer

class TimeHoursSerializer(ModelSerializer):
    class Meta:
        model = TimeHours
        fields = '__all__'