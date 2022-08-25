from gc import get_objects
from msilib.schema import Class
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import ImageRoom, Room,Customer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
import os
# Create your views here.

class ImageRoomView(generics.GenericAPIView):
    serializer_class = serializers.ImageRoomSerializer
    queryset = ImageRoom.objects.all()

    def get(self,request):
        images = ImageRoom.objects.all()
        serializer = self.serializer_class(instance=images,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        try:
            data = request.data
            images = request.FILES.getlist('images')
            for image in images:
                photo = ImageRoom.objects.create(
                    title=data['title'],
                    description=data['description'],
                    images=image,
                    room_id=data['room_id'],
                )
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ImageRoomIdView(generics.GenericAPIView):
    serializer_class = serializers.ImageRoomSerializer
    def get_object(self,pk):
        try:
            return ImageRoom.objects.get(pk=pk)
        except ImageRoom.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        image= self.get_object(pk)
        serializer=self.serializer_class(instance=image)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        image = self.get_object(pk)
        if os.path.isfile(image.images.path):
            os.remove(image.images.path)
        serializer = self.serializer_class(instance=image,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        image = self.get_object(pk)
        if os.path.isfile(image.images.path):
            os.remove(image.images.path)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)