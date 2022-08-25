from django.urls import path
from . import views
urlpatterns = [
    path('service-room/',views.DiscounView.as_view(),name='service_room'),
    path('service-room/<int:pk>',views.DiscountIdView.as_view(),name='detail_service_room'),
]
