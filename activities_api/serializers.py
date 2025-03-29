from rest_framework import serializers
from.models import WeatherForecast, Activity, UserPreference


class WeatherForecastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WeatherForecast
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


class UserPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPreference
        fields = '__all__'