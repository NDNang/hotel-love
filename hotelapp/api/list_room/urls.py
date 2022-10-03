from django.conf import settings
from django.urls import path,include
from . import views

urlpatterns = [
    path('room/',views.RoomView.as_view(),name='room'),
    path('room/<int:pk>',views.RoomIdView.as_view(),name='detail_room'),
    path('room-filter/',views.RoomFilter.as_view(),name='room_filters'),
    path('room-office/',views.ListRoomOffice.as_view(),name='ListRoomOffice'),
]