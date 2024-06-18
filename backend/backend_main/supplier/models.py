from django.db import models


# Create your models here.
class SupplierTable(models.Model):
    supplier_name = models.CharField(max_length=100, null=False)
    supplier_contact_info = models.CharField(max_length=255)
    supplier_address_line1 = models.CharField(max_length=255)
    supplier_address_line2 = models.CharField(max_length=255)
    supplier_city = models.CharField(max_length=100)
    supplier_state = models.CharField(max_length=100)
    supplier_postal_code = models.CharField(max_length=20)
    supplier_country = models.CharField(max_length=100)

    def __str__(self):
        return self.supplier_name
