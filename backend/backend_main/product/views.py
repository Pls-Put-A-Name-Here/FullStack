from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from .utils import store_image


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# View to handle the product image
@extend_schema(
    methods=["GET"],
    responses={200: ProductImageSerializer(many=True), 404: "Not Found"},
)
@extend_schema(
    methods=["POST"],
    request=ProductImageSerializer,
    responses={201: ProductImageSerializer, 400: "Bad Request", 404: "Not Found"},
)
@api_view(["GET", "POST"])
def ProductImageView(request, product_id=None):
    if request.method == "GET":
        if product_id is None:
            # Return all product images
            products = ProductImage.objects.all()
            serializer = ProductImageSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return images for a specific product
            product = get_object_or_404(Product, id=product_id)
            # Alternative way to get images
            # product_images = ProductImage.objects.filter(product_id=product)
            # productimage_set is a reverse relation from the product model
            # to the ProductImage model (i.e. product has a foreign key to ProductImage)
            product_images = product.productimage_set.all()
            serializer = ProductImageSerializer(product_images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        if "description" not in request.data or "image" not in request.FILES:
            return Response(
                {"error": "Description and image are required fields"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        description = request.data["description"]
        product = get_object_or_404(Product, id=product_id)
        image = request.FILES["image"]

        # Assume store_image is a utility function to handle image saving
        image_url = store_image(image)

        product_image = ProductImage.objects.create(
            product_id=product, url=image_url, description=description
        )
        serializer = ProductImageSerializer(product_image)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
