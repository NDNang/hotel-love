from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path('room/',views.RoomView.as_view(),name='room'),
    path('room/<int:pk>',views.RoomIdView.as_view(),name='detail_room'),
    path('room-filter/',views.RoomFilter.as_view(),name='room_filters')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)