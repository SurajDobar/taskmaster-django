from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemSerializers
from tasks.models import Task

@api_view(['GET'])
def getData(request):
    tasks = Task.objects.all()
    if request.query_params.get('completed'):
        tasks = tasks.filter(completed=True)
    serializer = ItemSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingle(request, pk):
    task = Task.objects.get(id=pk)
    serializer = ItemSerializers(task)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addData(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def editData(request, pk):
    task = Task.objects.get(id=pk)
    serializer = ItemSerializers(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteData(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response({'message': 'task deleted'})