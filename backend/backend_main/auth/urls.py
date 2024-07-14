from django.urls import path, include
# from rest_framework.routers import DefaultRouter

from . import views

# router.register(views.list_or_add, basename="cart")

urlpatterns = [
    path('register/', views.register, name='register' ),
    path('login/', views.login, name='login' ),
]