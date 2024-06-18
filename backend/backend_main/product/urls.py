from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductView, ProductImageView

router = DefaultRouter()
router.register(r"products", ProductView)


urlpatterns = [
    path("", include(router.urls)),
    path("product_images/", ProductImageView, name="product-image"),
    path("product_images/<int:product_id>/", ProductImageView, name="product-image"),
]
