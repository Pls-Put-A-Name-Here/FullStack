from . import models
from rest_framework import serializers


class UserSerialzers(serializers.ModelSerializer):

    class Meta:
        model= models.UserTable
        fields="__all__"
class UserAddressSerializers(serializers.ModelSerializer):

    class Meta:
        model= models.UserAddressTable
        fields="__all__"
