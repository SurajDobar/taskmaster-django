from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializers
from tasks.models import Task

# Create your views here.

#get data in response 
@api_view(['GET'])
def getData(request):
    Tasks=Task.objects.all()
    serializer=ItemSerializers(Tasks,many=True) 
    return Response(serializer.data)


#add data in response
@api_view(['POST'])
def addData(request):
    serializer=ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)