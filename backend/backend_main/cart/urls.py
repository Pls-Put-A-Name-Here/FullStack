from django.urls import path, include

# from rest_framework.routers import DefaultRouter

from . import views

# router.register(views.list_or_add, basename="cart")

urlpatterns = [
    path("cart/", views.list_or_add, name="list-or-add"),
]
