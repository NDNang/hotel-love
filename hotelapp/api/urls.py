from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .jwt import JWTTokenObtainPairView
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('room-view', views.RoomViewSet,basename='room_view')
urlpatterns = [
    path('token/', JWTTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('',include(router.urls)),
]
