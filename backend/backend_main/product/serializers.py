from rest_framework import serializers
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ["id", "upload_date", "last_edit_date", "product_id"]


class ProductSerializer(serializers.ModelSerializer):
    product_images = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_product_images(self, obj):
        images = obj.productimage_set.all()
        return ProductImageSerializer(images, many=True).data


# something cool from a stackoverflow post
# might be useful for adding extra fields to serializers
class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(
            declared_fields, info
        )

        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
