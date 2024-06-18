from rest_framework import serializers
from . import models


class CartSerializer(serializers.ModelSerializer):
    model = models.Cart
    fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    model = models.CartItem
    fields = "__all__"
