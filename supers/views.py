from functools import partial
from unicodedata import name
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Power, Super
from .serializers import SuperSerializer

# Create your views here.

class Supers_List(APIView):
    #gets all supers and returns JSON formatted response
    def get(self, request, format = None):
        supers = Super.objects.all()

        super_param = request.query_params.get('type')

        if super_param:
            supers = supers.filter(super_type__type=super_param)
        
        #create a dictionary
        supers_dictionary = {}
        #loop through the supers object
        for super in supers:
            #filters the supers object for the super_type
            super_types = Super.objects.filter(super_type__type=super.super_type.type)
            #serilizes the supers object into JSON
            serializer = SuperSerializer(super_types, many = True)
            #assigns the serialized data to the dictionary
            supers_dictionary[super.super_type.type]=serializer.data
            
        return Response(supers_dictionary, status = status.HTTP_200_OK)

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
    
    def patch(self, request, pk, format=None):
        super = self.get_object(pk)
        power_param = request.query_params.get('id')
        power = Power.objects.get(id=power_param)
        
        

        serializer = SuperSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)




"""
I was not able to solve the bonus question: steps I attempted:
- create power model
- migrated model, and registered with admin site. table was created and seeded with powers
- in the Super model I replaced the primary and secondary ability with manytomany field, pointing to the Power model. initially received a E304 Reverse accessor error, I 
assume this was fixed adding relative names to the line of code.
- I then built a patch method that
    - gets the super object by primary key
    - then gets the parameter from the URL
    - then gets the power object by id provided in the param
    
    - serializing the data is where I think I am missing something. I have tried many things, and googled quite a bit not identifying what is missing from my serializer. 
    Or if the error is with the relative names chosen. or both.
        - I reviewed the slides, and the django tutorial. As well as some other sites that popped up during the search. 

"""