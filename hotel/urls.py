
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('hotelapp.api.urls')),
    path('api/v1/', include('hotelapp.api.book_room.urls')),
    path('api/v1/', include('hotelapp.api.customer.urls')),
    path('api/v1/', include('hotelapp.api.discount.urls')),
    path('api/v1/', include('hotelapp.api.extra_service.urls')),
    path('api/v1/', include('hotelapp.api.image_room.urls')),
    path('api/v1/', include('hotelapp.api.list_room.urls')),
    path('api/v1/', include('hotelapp.api.service_room.urls')),
]
