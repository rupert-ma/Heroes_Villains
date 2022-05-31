from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Super
from .serializers import SuperSerializer



class Super_Type_List(APIView):
    pass


class Super_Type_Detail(APIView):
    pass