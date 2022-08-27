from django.urls import path
from . import views
urlpatterns = [
    path('discount/',views.DiscountView.as_view(),name='discount_room'),
    path('discount-room/<int:pk>',views.DiscountIdView.as_view(),name='detail_discount_room'),
]
