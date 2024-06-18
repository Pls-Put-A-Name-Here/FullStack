# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from . import models
from . import serializers


# Http404:
# get_object_or_404:
# DRF Imports:
# api_view:
# Response: status:
# status:

# Create your views here.
# FBVs

# This view handels the getting of all carts and the posting of anew cart item


@api_view(["GET", "POST"])
def list_or_add(request):
    if request.method == "GET":
        cart_model = models.Cart.objects.all()
        serializer = serializers.CartSerializer(cart_model, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        data = JSONParser.parse(request)
        serializer = serializers.CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
