from rest_framework import serializers
from . import models


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    
    class meta:
        model = models.CartItem
        fields = '__all__'
