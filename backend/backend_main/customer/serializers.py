from rest_framework import serializers
from customer.models import CustomerTable


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTable
        fields = "__all__"
