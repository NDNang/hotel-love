from django.urls import path
from . import views
urlpatterns = [
    path('customer/',views.CustomerView.as_view(),name='customer'),
    path('customer/<int:pk>',views.CustomerIdView.as_view(),name='detail_customer'),
]
