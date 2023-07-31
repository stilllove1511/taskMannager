# views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import List
from .serializers import ListSerializer

@api_view(['POST'])
def create_list(request):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_list(request):
    lists = List.objects.all()
    serializer = ListSerializer(lists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_list(request, id):
    list = List.objects.get(id=id)
    serializer = ListSerializer(instance=list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_list(request, id):
    list = List.objects.get(id=id)
    list.delete()
    return Response({'message': 'List deleted successfully!'},status=status.HTTP_204_NO_CONTENT)