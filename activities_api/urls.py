# travel_api/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ActivityListCreateView, ActivityDetailView, UserPreferenceView, WeatherForecastListView

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('user/preferences/', UserPreferenceView.as_view(), name='user-preferences'),
    path('weather/', WeatherForecastListView.as_view(), name='weather-forecast-list'),
    
    # Autenticação JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
