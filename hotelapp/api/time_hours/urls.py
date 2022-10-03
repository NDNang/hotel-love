from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

time_hours_list = views.TimeHoursView.as_view({
    'get': 'list',
    'post': 'create'
})
time_hours_detail = views.TimeHoursView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('time-hour/',time_hours_list,name='time_hour_book'),
    path('time-hour-detail/<int:pk>/',time_hours_detail,name='time_hour_detail')
]