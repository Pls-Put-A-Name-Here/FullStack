from django.db import models


# Create your models here.
class Inventory(models.Model):
    invIdpk = models.AutoField(primary_key=True)
    invPrdIdfk = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    invQuantityAvailable = models.IntegerField()
    invUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    invUnitCost = models.DecimalField(max_digits=10, decimal_places=2)
    invSupIdfk = models.ForeignKey("supplier.SupplierTable", on_delete=models.CASCADE)
    invDateAdded = models.DateTimeField()
    invExpirationDate = models.DateTimeField()
    invLastUpdateDate = models.DateTimeField(auto_now=True)
