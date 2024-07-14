# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes, authentication_classes

from . import models
from . import serializers


# Http404:
# get_object_or_404: 
# DRF Imports:
# api_view: 
# Response: 
# status:

# Create your views here.
# FBVs

# This view habdles the getting of all carts and the posting of anew cart item

@api_view(['GET', 'POST'])
# @authentication_classes([ BasicAuthentication])
# @permission_classes([IsAuthenticated])
def list_or_add(request):
    if request.method == 'GET':
        cart_model = models.Cart.objects.all()
        serializer = serializers.CartSerializer(cart_model, many=True)

    #     content = {
    #     'user': str(request.user),  # `django.contrib.auth.User` instance.
    #     'auth': str(request.auth),  # None
    # }
        # print(content)
        return Response( serializer.data)
        # return Response( content)
    
    if request.method == 'POST':
        data = request.data
        # data.crtCustomerIdfk = int(data.crtCustomerIdfk)
        serializer = serializers.CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return(Response(serializer.data, status=201))
        return(Response(serializer.errors, status=400))
    
    # This view handles the retrievea a single entry, updates an entry and deletes an entry
@api_view(['GET', 'PATCH', 'DELETE'])
def single_entry_operation(request, pk):
    try: 
        get_cart = models.Cart.objects.get(pk=pk)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':                     #Url Format http://127.0.0.1:8000/api/cart/?pk={primary_key}
        serializer = serializers.CartSerializer(get_cart, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = serializers.CartSerializer(get_cart, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        get_cart.delete()
        return Response({"message" : "Deleted Sucessfuly"}, status=status.HTTP_200_OK)