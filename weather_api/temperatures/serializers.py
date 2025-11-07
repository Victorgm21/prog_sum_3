from rest_framework import serializers

from .models import cityTemperature

class cityTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = cityTemperature
        fields = '__all__'