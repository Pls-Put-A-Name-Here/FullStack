from django.urls import path, include
# from rest_framework.routers import DefaultRouter

from . import views

# router.register(views.list_or_add, basename="cart")

urlpatterns = [
    path('api/cart/', views.list_or_add, name='list-or-add' ),
    path('api/cart/<int:pk>/', views.single_entry_operation, name='seo')
]