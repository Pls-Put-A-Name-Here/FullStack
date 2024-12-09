from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from product import urls as productUrls
from customer import urls as customerUrls
from cart import urls as cartUrls
from auth import urls as authUrls
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("product.urls")),
    path("api/v1/", include("customer.urls")),
    path("api/v1/", include("cart.urls")),
    path("api/v1/", include("order.urls")),
    path("api/v1/", include("payments.urls")),
    path("api/v1/customer/", include(customerUrls)),
    path("", include(cartUrls)),
    path("r/", include(authUrls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
