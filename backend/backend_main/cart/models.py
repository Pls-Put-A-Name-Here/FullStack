from django.db import models


# Create your models here.
# This the models for tblCarts
class Cart(models.Model):
    crtIdpk = models.AutoField(primary_key=True, db_column="crtIdpk")
    crtCustomerIdfk = models.ForeignKey(
        "customer.CustomerTable", on_delete=models.CASCADE, db_column="crtCustomerIdfk"
    )
    crtCreatedAt = models.DateTimeField(auto_now_add=True, db_column="crtCreatedAt")
    crtStatus = models.CharField(max_length=50, default="Active", db_column="crtStatus")

    class Meta:
        db_table = "tblCarts"
        managed = False


# This the models for tblCartItems
class CartItem(models.Model):
    crtItemIdpk = models.AutoField(primary_key=True, db_column="crtItemIdpk")
    crtItemCrtIdfk = models.ForeignKey(
        "Cart", on_delete=models.CASCADE, db_column="crtItemCrtIdfk"
    )
    crtItemPrdIdfk = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, db_column="crtItemPrdIdfk"
    )
    crtItemQuantity = models.IntegerField(db_column="crtItemQuantity")
    crtItemUnitPrice = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="crtItemUnitPrice"
    )

    class Meta:
        db_table = "tblCartItems"
        managed = False
