from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import ItemSerializers
from tasks.models import Task

# Create your views here.

#get data in response 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getData(request):
    tasks = Task.objects.filter(user=request.user)
    serializer = ItemSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSingle(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    serializer = ItemSerializers(task)
    return Response(serializer.data)

#add data in response
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addData(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

#edit data in response 
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def editData(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    serializer = ItemSerializers(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete data in response 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteData(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()
    return Response({'message': 'task deleted'})