from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


type_book_list = views.TypeBookView.as_view({
    'get': 'list',
    'post': 'create'
})
type_book_detail = views.TypeBookView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('type-book/',type_book_list,name='type_book'),
    path('type-book-detail/<int:pk>/',type_book_list,name='type_book_detail')
]