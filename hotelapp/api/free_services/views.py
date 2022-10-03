from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
import os
from django.db.models import Q
from hotelapp.models import FreeServiceRoom
from rest_framework.response import Response
# Create your views here.

class FreeServiceRoomView(viewsets.ModelViewSet):
    queryset = FreeServiceRoom.objects.all()
    serializer_class = serializers.FreeServiceRoomSerializer

    