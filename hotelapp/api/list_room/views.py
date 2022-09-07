from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import Room,BookRoom
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
        room_id = BookRoom.objects.values_list('room_id',flat=True).filter((Q(date_in__range=(date_in, date_out)) | Q(date_out__range=(date_in, date_out))) & (Q(status=True)))
        data = Room.objects.filter(~Q(pk__in = set(room_id)))
        serializer = self.serializer_class(instance=data,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
       