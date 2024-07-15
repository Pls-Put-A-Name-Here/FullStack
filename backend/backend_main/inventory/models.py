from django.db import models


# Create your models here.
class Inventory(models.Model):
    invIdpk = models.AutoField(primary_key=True, db_column="invIdpk")
    invPrdIdfk = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, db_column="invPrdIdfk"
    )
    invQuantityAvailable = models.IntegerField(db_column="invQuantityAvailable")
    invUnitPrice = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="invUnitPrice"
    )
    invUnitCost = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="invUnitCost"
    )
    invSupIdfk = models.ForeignKey(
        "supplier.SupplierTable", on_delete=models.CASCADE, db_column="invSupIdfk"
    )
    invDateAdded = models.DateTimeField(db_column="invDateAdded")
    invExpirationDate = models.DateTimeField(db_column="invExpirationDate")
    invLastUpdateDate = models.DateTimeField(
        auto_now=True, db_column="invLastUpdateDate"
    )

    class Meta:
        db_table = "tblInventory"
        managed = False
