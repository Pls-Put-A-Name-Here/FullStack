from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

from . import models
from . import serializers


@api_view(['GET', 'POST'])
@extend_schema(
    methods=['GET'],
    responses={200: serializers.CartSerializer(many=True)}
)
@extend_schema(
    methods=['POST'],
    request=serializers.CartSerializer,
    responses={201: serializers.CartSerializer, 400: "Error message"}
)
def list_or_add(request):
    if request.method == 'GET':
        cart_model = models.Cart.objects.all()
        serializer = serializers.CartSerializer(cart_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = serializers.CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
