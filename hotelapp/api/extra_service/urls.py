from django.urls import path
from . import views
urlpatterns = [
    path('extra-service/',views.ExtraServiceView.as_view(),name='extra_service'),
    path('extra-service/<int:pk>',views.ExtraServiceIdView.as_view(),name='detail_extra_service'),
]
