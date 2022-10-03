from django.urls import path
from . import views

urlpatterns = [
    path('book-room/',views.BookRoomView.as_view(),name='book_room'),
    path('book-room/<int:pk>',views.BookRoomIdView.as_view(),name='detail_book_room'),
    path('book-room-status/<int:pk>',views.BookRoomIdStatus.as_view(),name='detail_book_room_status'),
    path('book-room-office/',views.BookRoomOffice.as_view(),name='detail_book_room_status'),
]
