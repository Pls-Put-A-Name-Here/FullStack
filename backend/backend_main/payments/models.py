import uuid
from django.db import models
from core.models import User


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="GHS")
    transaction_id = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("PENDING", "Pending"),
            ("COMPLETED", "Completed"),
            ("FAILED", "Failed"),
        ],
        default="PENDING",
    )

    def __str__(self):
        return f"{self.user.user_name} - {self.amount} {self.currency}"

    class Meta:
        db_table = "tblPayments"
        managed = True


class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tblPaymentMethods"
        managed = True

    def __str__(self):
        return self.name


class PaymentStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tblPaymentStatuses"
        managed = True


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tblPurchases"
        managed = True

    def __str__(self):
        return f"Purchase {self.id} by {self.customer}"
