from gc import get_objects
from django.shortcuts import render
from rest_framework import generics,viewsets,status
from . import serializers
from hotelapp.models import Code
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
import os
from django.db.models import Q
import random, string
# Create your views here.

class CodeView(generics.GenericAPIView):
    serializer_class = serializers.CodeSerializer
    
    def get(self,request):
        code_id,code_name = self.render_code()
        return Response(data={"id":code_id,"code":code_name},status=status.HTTP_200_OK)
    
    def render_code(self):
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(characters) for i in range(6))
        is_exists = Code.objects.filter(name=code).count()
        if is_exists:
            self.render_code()
        else:
            sv_code = Code(name=code)
            sv_code.save()
            code_id = sv_code.id
            code_name = sv_code.name
        
        return code_id,code_name
