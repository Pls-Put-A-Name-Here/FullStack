from django.db import models


# Create your models here.
# This the models for tblCarts
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True,db_column='crtIdpk')
    cart_customer_id = models.ForeignKey('customer.Customer', on_delete=models.CASCADE,db_column="crtCustomerIdfk")
    created_at = models.DateTimeField(auto_now_add=True,db_column="crtCreatedAt")
    cart_status = models.CharField(max_length=50, default='Active',db_column="crtStatus")
    
    class Meta:
        db_table='tblCarts'
        managed = False

# This the models for tblCartItems


class CartItem(models.Model):
    crtItemIdpk = models.AutoField(primary_key=True)
    crtItemCrtIdfk = models.ForeignKey('Cart', on_delete=models.CASCADE)
    crtItemPrdIdfk = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    crtItemQuantity = models.IntegerField()
    crtItemUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    class meta:
        db_table='tblCartItems'
        managed=False
        