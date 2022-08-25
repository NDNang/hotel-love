from gc import get_objects
from msilib.schema import Class
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import ServiceRoom
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
# Create your views here.

class ServiceRoomView(generics.GenericAPIView):
    serializer_class = serializers.ServiceRoomSerializer
    queryset = ServiceRoom.objects.all()

    def get(self,request):
        service_rooms = ServiceRoom.objects.all()
        serializer = self.serializer_class(instance=service_rooms,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ServiceRoomIdView(generics.GenericAPIView):
    serializer_class = serializers.ServiceRoomSerializer
    def get_object(self,pk):
        try:
            return ServiceRoom.objects.get(pk=pk)
        except ServiceRoom.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        service_rooms= self.get_object(pk)
        serializer=self.serializer_class(instance=service_rooms)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        service_rooms = self.get_object(pk)
        serializer = self.serializer_class(instance=service_rooms,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        service_rooms = self.get_object(pk)
        service_rooms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



