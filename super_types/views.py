from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import SuperType
from .serializers import SuperTypeSerializer
from supers import serializers

# Create your views here.

class Super_Types_List(APIView):
    def get():
        pass

class Super_Types_Detail(APIView):
    pass


