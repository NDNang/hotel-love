from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import Discount
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
# Create your views here.

class DiscounView(generics.GenericAPIView):
    serializer_class = serializers.DiscountSerializer
    queryset = Discount.objects.all()

    def get(self,request):
        discounts = Discount.objects.all()
        serializer = self.serializer_class(instance=discounts,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DiscountIdView(generics.GenericAPIView):
    serializer_class = serializers.Discount
    def get_object(self,pk):
        try:
            return Discount.objects.get(pk=pk)
        except Discount.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        discounts= self.get_object(pk)
        serializer=self.serializer_class(instance=discounts)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        discounts = self.get_object(pk)
        serializer = self.serializer_class(instance=discounts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        discounts = self.get_object(pk)
        discounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



