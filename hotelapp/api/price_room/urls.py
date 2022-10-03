from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


price_room_list = views.PriceRoomView.as_view({
    'get': 'list',
    'post': 'create'
})
price_room_detail = views.PriceRoomView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('price-room/',price_room_list,name='price_room'),
    path('price-room-detail/<int:pk>/',price_room_detail,name='price_room_detail')
]