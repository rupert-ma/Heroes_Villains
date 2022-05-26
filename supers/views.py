from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Super
from .serializers import SuperSerializer

# Create your views here.

class Supers_List(APIView):
    #gets all supers and returns JSON formatted response
    def get(self, request, format = None):
        supers = Super.objects.all()

        super_param = request.query_params.get('type')

        if super_param:
            supers = supers.filter(super_type__type=super_param)

        serializer = SuperSerializer(supers, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    #creates new super 
    def post(self, request, format = None):
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class Supers_Detail(APIView):
    
    def get_object(self, pk):
        try:
            return Super.objects.get(pk = pk)
        except Super.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        super = self.get_object(pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format = None):
        super = self.get_object(pk)
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        super = self.get_object(pk)
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

