from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

# from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, authentication_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from core.serializers import UserAddressSerializers, UserSerialzers


@api_view(["POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def register(request):
    data = request.data
    serializer = UserSerialzers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("usrName")
    password = request.data.get("usrPassword")
    user = authenticate(username=username, password=password)
    if user:
        return Response(
            {"message": "Authentication Successfull"}, status=status.HTTP_200_OK
        )
    return Response(
        {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
    )
