from tkinter.messagebox import NO
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import SuperType
from .serializers import SuperTypeSerializer



class Super_Type_List(APIView):
    
    def get(self, request, format = None):
        super_types = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_types, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format = None):
        serializer = SuperTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class Super_Type_Detail(APIView):
    def get_object(self, pk):
        try:
            return SuperType.objects.get(pk=pk)
        except SuperType.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        super_type = self.get_object(pk)
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
