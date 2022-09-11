from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import Room,BookRoom,Discount,ImageRoom
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
import os
from django.db.models import Q
from datetime import datetime
# Create your views here.

class RoomView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.RoomSerializer
    queryset = Room.objects.all()
    def get(self,request):
        rooms = Room.objects.all()
        serializer = self.serializer_class(instance=rooms,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RoomIdView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RoomSerializer
    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        room= self.get_object(pk)
        serializer=self.serializer_class(instance=room)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        room = self.get_object(pk)
        if os.path.isfile(room.images.path):
            os.remove(room.images.path)
        serializer = self.serializer_class(instance=room,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        room = self.get_object(pk)
        if os.path.isfile(room.images.path):
            os.remove(room.images.path)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RoomFilter(generics.GenericAPIView):
    serializer_class = serializers.RoomViewSerializer
    queryset = Room.objects.all()
    def get(self,request):
        queryprms = request.GET
        date_in = datetime.strptime(queryprms.get('date_in'),'%Y-%m-%dT%H:%M:%SZ')
        date_out = datetime.strptime(queryprms.get('date_out'),'%Y-%m-%dT%H:%M:%SZ')
        room_id = BookRoom.objects.filter((Q(date_in__range=(date_in, date_out)) | Q(date_out__range=(date_in, date_out))) & (Q(status=True))).values_list('room_id',flat=True)
        data = Room.objects.filter(~Q(pk__in = set(room_id)))
        serializer = self.serializer_class(instance=data,many = True)
        
        ls_data =[]
        for item in serializer.data:
            percent = 0
            date_start =""
            date_end =""
            discount = Discount.objects.filter(room_id = item['id'],status=True).values()
            if discount:
                percent = int(discount[0]['percent'])
                date_start =discount[0]['date_start'].strftime('%d/%m/%Y %H:%M:%S')
                date_end =discount[0]['date_end'].strftime('%d/%m/%Y %H:%M:%S')
            price = float(item['price'])
            total = round(price - (price*percent/100))
            image_rooms = ImageRoom.objects.filter(room_id = item['id'],status=True).values()
            ls_images = []
            images = {}
            for img in image_rooms:
                url = 'static/images'+img['images']
                images={'id':img['id'],'title':item['title'],'url':url}
                ls_images.append(images)
            obj ={'id':item['id'],'name':item['name'],'title':item['title'],'description':item['description'],'type':item['type'],'price':'{:0,.0f}'.format(price),'images':item['images'],'total':'{:0,.0f}'.format(total),'discount':percent,'date_start':date_start,'date_end':date_end,'ls_images':ls_images}
            ls_data.append(obj)
        return Response(data=ls_data,status=status.HTTP_200_OK)
       