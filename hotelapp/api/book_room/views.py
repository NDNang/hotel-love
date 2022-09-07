from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import BookRoom,Customer, Room,ExtraService
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from django.db import DatabaseError, transaction
# Create your views here.

class BookRoomView(generics.GenericAPIView):
    serializer_class = serializers.BookRoomSerializer
    queryset = BookRoom.objects.all()

    def get(self,request):
        book_rooms = BookRoom.objects.filter(status=True).order_by('date_in', 'date_out')
        serializer = self.serializer_class(instance=book_rooms,many = True)
        data = []
        for item in serializer.data:
            arr_service_name =[]
            obj = {'id':item['id'],'fullname':item['fullname'],'phone':item['phone'],'room':item['room_name'],
            'date_in':item['date_in'],'date_out':item['date_out'],'code':item['code_name'],'total':item['total'],'is_pay':item['is_pay']}
            for val in item['extra_service']:
                service = ExtraService.objects.filter(pk=val).values('id','name')
                arr_service_name.append(service)
            obj['extra_service']  = arr_service_name  
            data.append(obj)
        return Response(data=data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        customer = Customer.objects.filter(phone = data['phone']).values('id')
        data._mutable = True
        try:
            with transaction.atomic():
                if customer:
                    data['customer'] = customer[0]['id']
                else:
                    cus = Customer(fullname = data['fullname'],phone=data['phone'])
                    cus.save()
                    data['customer'] = cus.id
            
                serializer = self.serializer_class(data=data)
                if serializer.is_valid():
                    serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        except DatabaseError:
            transaction.rollback()
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookRoomIdView(generics.GenericAPIView):
    serializer_class = serializers.BookRoomSerializer
    def get_object(self,pk):
        try:
            return BookRoom.objects.get(pk=pk)
        except BookRoom.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        book_rooms= self.get_object(pk)
        serializer=self.serializer_class(instance=book_rooms)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        book_rooms = self.get_object(pk)
        serializer = self.serializer_class(instance=book_rooms,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        book_rooms = self.get_object(pk)
        book_rooms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookRoomIdStatus(generics.GenericAPIView):
    serializer_class = serializers.BookRoomStatusSerializer
    def put(self,request,pk):
        try:
            with transaction.atomic():
                book_room = BookRoom.objects.get(pk=pk)
                serializer = self.serializer_class(instance=book_room,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    customer = Customer.objects.get(pk=book_room.customer_id)
                    if serializer.data['is_pay']:
                        customer.sum_success = int(customer.sum_success)+1
                    else:
                        customer.sum_fail =int(customer.sum_fail)+1
                    customer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except DatabaseError:
            transaction.rollback()
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


