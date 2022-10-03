from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
import os
from django.db.models import Q
from hotelapp.models import TypeBook
from rest_framework.response import Response
# Create your views here.

class TypeBookView(viewsets.ModelViewSet):
    queryset = TypeBook.objects.all()
    serializer_class = serializers.TypeBookSerializer

    