from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from order.models import Order
from core.models import User
import requests, json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from drf_spectacular.utils import extend_schema


@permission_classes([IsAuthenticated])
@extend_schema(
    request=None,
    responses={
        200: {"authorization_url": "URL to redirect user for payment"},
        400: {"error": "Error initializing payment"},
    },
)
@api_view(["POST"])
def initiate_payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    amount = int(order.total_cost * 100)
    user = request.user
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "email": user.email,
        "amount": amount,
        "reference": f"ECOM_{order.id}",
        "callback_url": request.build_absolute_uri("/api/v1/payments/callback/"),
    }
    response = requests.post(
        "https://api.paystack.co/transaction/initialize",
        headers=headers,
        data=json.dumps(data),
    )
    if response.status_code == 200:
        response_data = response.json()
        authorization_url = response_data["data"]["authorization_url"]
        return JsonResponse({"authorization_url": authorization_url})
    else:
        return JsonResponse(
            {"error": "Error initializing payment"}, status=response.status_code
        )


@extend_schema(
    request=None,
    responses={
        200: {"status": "success", "order_id": "ID of the order"},
        400: {"status": "failed", "error": "Error message"},
        500: {"status": "failed", "error": "Verification failed"},
    },
)
@api_view(["GET"])
def payment_callback_view(request):
    reference = request.GET.get("reference")
    headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
    response = requests.get(
        f"https://api.paystack.co/transaction/verify/{reference}", headers=headers
    )
    if response.status_code == 200:
        response_data = response.json()
        if response_data["data"]["status"] == "success":
            order_id = reference.split("_")[1]
            order = get_object_or_404(Order, id=order_id)
            if response_data["data"]["amount"] == int(order.total_cost * 100):
                order.status = "PAID"
                order.save()
                return JsonResponse({"status": "success", "order_id": order_id})
            else:
                return JsonResponse(
                    {"status": "failed", "error": "Amount mismatch"}, status=400
                )
        else:
            return JsonResponse(
                {"status": "failed", "error": "Payment failed"}, status=400
            )
    else:
        return JsonResponse(
            {"status": "failed", "error": "Verification failed"}, status=500
        )


@extend_schema(
    request=None, responses={200: {"status": "success", "order": "ID of the order"}}
)
@api_view(["GET"])
def payment_success_view(request):
    reference = request.GET.get("reference")
    order = get_object_or_404(Order, id=reference.split("_")[1])
    return JsonResponse({"status": "success", "order": order.id})


@extend_schema(request=None, responses={200: {"status": "failed"}})
@api_view(["GET"])
def payment_failure_view(request):
    return JsonResponse({"status": "failed"})
