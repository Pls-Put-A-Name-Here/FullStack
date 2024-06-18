from rest_framework import serializers
from .models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    # fetch the product images
    # since the product images are a related field, we need to use the SerializerMethodField
    product_images = serializers.SerializerMethodField()

    # fetch other related fields using prefetch_related
    brand = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"

    # might have to optimize this later
    # takes about 6 seconds to load 1000 products
    # by default, the SerializerMethodField will look for a method called get_<field_name>
    def get_product_images(self, obj):
        images = obj.productimage_set.all()
        return ProductImageSerializer(images, many=True).data


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


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
