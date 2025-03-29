from django.contrib import admin
from .models import Activity, WeatherForecast, UserPreference

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('city', 'date', 'temperature', 'humidity', )
