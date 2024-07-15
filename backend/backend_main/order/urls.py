from django.urls import path
from .views import orders, order_items, order_detail, order_status, order_statuses

urlpatterns = [
    path("orders/", orders, name="orders"),
    path("orders/statuses/", order_statuses, name="order_statuses"),
    path("orders/<uuid:pk>/", order_detail, name="order_detail"),
    path("orders/<uuid:pk>/status/", order_status, name="order_status"),
    path("orders/<uuid:pk>/items/", order_items, name="order_items"),
]
