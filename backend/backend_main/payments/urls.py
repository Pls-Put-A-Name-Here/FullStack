from django.urls import path
from .views import (
    initiate_payment,
    payment_callback_view,
    payment_success_view,
    payment_failure_view,
)

urlpatterns = [
    path(
        "payments/initiate/<uuid:order_id>/", initiate_payment, name="initiate_payment"
    ),
    path("paymnts/callback/", payment_callback_view, name="payment_callback"),
    path("payments/success/", payment_success_view, name="payment_success"),
    path("payments/failure/", payment_failure_view, name="payment_failure"),
]
