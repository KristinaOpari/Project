from django.shortcuts import render
from .models import *
from .forms import *
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework import viewsets


@api_view(['POST'])
@renderer_classes([BrowsableAPIRenderer])
def createUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def showUser(request):
    query_set=User.objects.all()
    return Response({'users':query_set},template_name='show_user.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.flag=0
    return Response("User Deleted Successfully")
