import uuid
from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,db_column="ordId")
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE,db_column="ordCustomerIdfk")
    delivery_address = models.CharField(max_length=255,db_column="ordDeliveryAddress")
    total_cost = models.DecimalField(max_digits=10, decimal_places=2,db_column="ordTotalCost")
    status = models.ForeignKey('OrderStatus', default="1", on_delete=models.CASCADE,db_column="ordStatusIdfk")
    created_date = models.DateTimeField(auto_now_add=True,db_column="ordCreatedDate")
    last_edited_date = models.DateTimeField(auto_now=True,db_column="ordLastEditedDate")

    def __str__(self):
        return f"Order {self.id} for {self.customer}"

    @staticmethod
    def create_order(customer, delivery_address, status):
        order_id = uuid.uuid4()
        order = Order.objects.create(
            id=order_id,
            customer=customer,
            delivery_address=delivery_address,
            status=status
        )
        return order

    class Meta:
        db_table = "tblOrders"
        managed = False


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,db_column="ordtId")
    order = models.ForeignKey('Order', related_name="order_items", on_delete=models.CASCADE,db_column="ordtOrdIdfk")
    product = models.ForeignKey('product.Product', related_name="product_orders", on_delete=models.CASCADE,db_column="ordtPrdIdfk")
    quantity = models.PositiveIntegerField(db_column="ordtQuantity")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,db_column="ordtUnitPrice")
    total_price = models.DecimalField(max_digits=10, decimal_places=2,db_column="ordtSubtotal")
    created_date = models.DateTimeField(auto_now_add=True,db_column="ordCreatedDate")
    last_edited_date = models.DateTimeField(auto_now=True,db_column="ordLastEditedDate")

    def __str__(self):
        return f"Item {self.id} for Order {self.order.id}"

    @staticmethod
    def create_order_item(order, product, quantity, unit_price, total_price):
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price
        )
        return order_item

    class Meta:
        db_table = "tblOrderItems"
        managed = False


class OrderStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,db_column="ordStatusId")
    name = models.CharField(max_length=50,db_column="ordStatusName")
    description = models.TextField(max_length=500,db_column="ordStatusDescription")
    created_date = models.DateTimeField(auto_now_add=True,db_column="ordStatusCreatedDate")
    last_edited_date = models.DateTimeField(auto_now=True,db_column="ordStatusLastEditedDate")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tblOrderStatuses"
        managed = False
