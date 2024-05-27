from django.db import models

# Create your models here.
class OrderTable(models.Model):
    ordIdpk = models.AutoField(primary_key=True, db_column='ordIdpk')
    ordCustIdpk = models.ForeignKey('customer.CustomerTable', on_delete=models.CASCADE, db_column='ordCustIdpk')
    ordDate = models.DateTimeField(auto_now_add=True, db_column='ordDate')
    ordDeliveryAddress = models.CharField(max_length=255, db_column='ordDeliveryAddress')
    ordTotalCost = models.DecimalField(max_digits=10, decimal_places=2, db_column='ordTotalCost')
    ordStatusIdfk = models.ForeignKey('order.OrderStatusTable', on_delete=models.CASCADE, db_column='ordStatusIdfk')
    ordStatusCreatedDate = models.DateTimeField(auto_now_add=True, db_column='ordStatusCreatedDate')
    LastUpdateDate = models.DateTimeField(auto_now=True, db_column='LastUpdateDate')

    def __str__(self):
        return str(self.ordIdpk)

    class Meta:
        db_table = "tblOrders"
        managed = False

class OrderItemsTable(models.Model):
    ordtIdpk = models.AutoField(primary_key=True, db_column='ordtIdpk')
    ordtOrdIdfk = models.ForeignKey('order.OrderTable', on_delete=models.CASCADE, db_column='ordtOrdIdfk')
    ordtPrdIdfk = models.ForeignKey('product.Product', on_delete=models.CASCADE, db_column='ordtPrdIdfk')
    ordtQuantity = models.IntegerField(db_column='ordtQuantity')
    ordtUnitPrice = models.DecimalField(max_digits=10, decimal_places=2, db_column='ordtUnitPrice')
    ordtSubtotal = models.DecimalField(max_digits=10, decimal_places=2, db_column='ordtSubtotal')
    ordtCreatedDate = models.DateTimeField(auto_now_add=True, db_column='ordtCreatedDate')
    ordtLastUpdateDate = models.DateTimeField(auto_now=True, db_column='ordtLastUpdateDate')

    def __str__(self):
        return str(self.ordtIdpk)
    
    class Meta:
        db_table = "tblOrderItem"
        managed = False
    
class OrderStatusTable(models.Model):
    ordStatusIdpk = models.AutoField(primary_key=True, db_column='ordStatusIdpk')
    ordStatusName = models.CharField(max_length=50, db_column='ordStatusName')
    ordStatusDescription = models.TextField(db_column='ordStatusDescription')
    ordStatusCreatedDate = models.DateTimeField(auto_now_add=True, db_column='ordStatusCreatedDate')
    ordStatusLastEditDate = models.DateTimeField(auto_now=True, db_column='ordStatusLastEditDate')

    def __str__(self):
        return self.ordStatusName
    
    class Meta:
        db_table = "tblOrderStatuses"
        managed = False
