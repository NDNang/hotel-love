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
    path('', include('hotelapp.api.book_room.urls')),
    path('', include('hotelapp.api.customer.urls')),
    path('', include('hotelapp.api.discount.urls')),
    path('', include('hotelapp.api.extra_service.urls')),
    path('', include('hotelapp.api.image_room.urls')),
    path('', include('hotelapp.api.list_room.urls')),
    path('', include('hotelapp.api.render_code.urls')),
    path('', include('hotelapp.api.time_hours.urls')),
    path('', include('hotelapp.api.type_book.urls')),
    path('', include('hotelapp.api.price_room.urls')),
    path('', include('hotelapp.api.free_services.urls')),
    # path('',include(router.urls)),
]
