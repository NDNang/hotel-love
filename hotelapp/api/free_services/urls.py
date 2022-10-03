from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


free_service_list = views.FreeServiceRoomView.as_view({
    'get': 'list',
    'post': 'create'
})
free_service_detail = views.FreeServiceRoomView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('free-service/',free_service_list,name='free_service'),
    path('free-service-detail/<int:pk>/',free_service_detail,name='free_service_detail')
]