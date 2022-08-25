from django.urls import path
from . import views
urlpatterns = [
    path('service-room/',views.ServiceRoomView.as_view(),name='service_room'),
    path('service-room/<int:pk>',views.ServiceRoomIdView.as_view(),name='detail_service_room'),
]
