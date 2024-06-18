from django.db import models


# Create your models here.
# This the models for tblCarts
class Cart(models.Model):
    crtIdpk = models.AutoField(primary_key=True)
    crtCustomerIdfk = models.ForeignKey(
        "customer.CustomerTable", on_delete=models.CASCADE
    )
    crtCreatedAt = models.DateTimeField(auto_now_add=True)
    crtStatus = models.CharField(max_length=50, default="Active")


# This the models for tblCartItems


class CartItem(models.Model):
    crtItemIdpk = models.AutoField(primary_key=True)
    crtItemCrtIdfk = models.ForeignKey("Cart", on_delete=models.CASCADE)
    crtItemPrdIdfk = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    crtItemQuantity = models.IntegerField()
    crtItemUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
