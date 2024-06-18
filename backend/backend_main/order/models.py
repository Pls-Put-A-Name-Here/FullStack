from django.db import models


# Create your models here.
class OrderTable(models.Model):
    order_customer_id = models.ForeignKey(
        "customer.CustomerTable", on_delete=models.CASCADE
    )
    order_date = models.DateTimeField(auto_now_add=True)
    order_delivery_address = models.CharField(max_length=255)
    order_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey("order.OrderStatusTable", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order_customer_id)


# This is the model for Order Items table
class OrderItemsTable(models.Model):
    order_id = models.ForeignKey("order.OrderTable", on_delete=models.CASCADE)
    product_id = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order_id)


# This is the model for Order status table
class OrderStatusTable(models.Model):
    order_status_name = models.CharField(max_length=50)
    order_status_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_status_name
