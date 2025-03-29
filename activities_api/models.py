from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_activities = models.ManyToManyField(Activity)
    preferred_weather = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Preferências de {self.user.username}"

class WeatherForecast(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Previsão para {self.city} em {self.date}"

