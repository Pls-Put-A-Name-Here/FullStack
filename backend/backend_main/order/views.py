import uuid

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from customer.models import Customer
from product.models import Product
from .models import OrderItem, Order, OrderStatus
from .serializers import OrderSerializer, OrderStatusSerializer, OrderItemSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(
    methods=["GET", "POST"],
    request=OrderSerializer,
    responses={
        200: OrderSerializer,
        201: OrderItemSerializer,
        400: "Product out of stock",
    },
)
@api_view(["GET", "POST"])
def orders(request, pk=None):
    if request.method == "GET":
        result = Order.objects.all()
        serializer = OrderSerializer(result, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        customer = get_object_or_404(Customer, pk=request.user.id)
        address = customer.address_id
        product = get_object_or_404(Product, pk=pk)

        if product.stock_quantity == 0:
            return Response(
                {"error": "Product out of stock", "product_id": product.id},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_id = uuid.uuid4()
        quantity = request.data.get("quantity", 0)
        price = product.unit_price
        order_status_ = OrderStatus.objects.get(status="paid")
        total = quantity * price

        order = Order.objects.create(
            customer=customer, order_id=order_id, address=address, status=order_status_
        )

        order_item = OrderItem.objects.create(
            order=order, product=product, quantity=quantity, price=price, total=total
        )

        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(
    methods=["GET", "PUT", "DELETE"],
    responses={"GET": OrderSerializer, "PUT": OrderStatusSerializer, "DELETE": None},
)
@api_view(["GET", "PUT", "DELETE"])
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = OrderStatusSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(
    methods=["GET", "POST"],
    request=OrderStatusSerializer,
    responses={"GET": OrderStatusSerializer, "POST": OrderStatusSerializer},
)
@api_view(["GET", "POST"])
def order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "GET":
        serializer = OrderStatusSerializer(order)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = OrderStatusSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(
    methods=["GET", "PUT", "DELETE"],
    responses={
        "GET": OrderStatusSerializer,
        "PUT": OrderStatusSerializer,
        "DELETE": None,
    },
)
@api_view(["GET", "PUT", "DELETE"])
def order_statuses(request, pk=None):
    if pk is None:
        if request.method == "GET":
            result = OrderStatus.objects.all()
            serializer = OrderStatusSerializer(result, many=True)
            return Response(serializer.data)
    else:
        order_status = get_object_or_404(OrderStatus, pk=pk)

        if request.method == "GET":
            serializer = OrderStatusSerializer(order_status)
            return Response(serializer.data)

        elif request.method == "PUT":
            serializer = OrderStatusSerializer(order_status, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            order_status.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(
    methods=["GET", "POST"],
    request=OrderSerializer,
    responses={"GET": OrderItemSerializer, "POST": OrderItemSerializer},
)
@api_view(["GET", "POST"])
def order_items(request, pk):
    if request.method == "GET":
        order = get_object_or_404(Order, pk=pk)
        result = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(result)
        return Response(serializer.data)

    elif request.method == "POST":
        order_item = get_object_or_404(OrderItem, pk=pk)
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {"error": serializer.errors, "order_item_id": order_item.id},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
