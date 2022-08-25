from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path('image-room/',views.ImageRoomView.as_view(),name='image_room'),
    path('image-room/<int:pk>',views.ImageRoomIdView.as_view(),name='detail_image_room'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)