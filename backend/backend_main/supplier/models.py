from django.db import models

# Create your models here.
class SupplierTable(models.Model):
    supIdpk = models.AutoField(primary_key=True, db_column='supIdpk')
    supName = models.CharField(max_length=100, null=False, db_column='supName')
    supContactInfo = models.CharField(max_length=255, db_column='supContactInfo')
    supAddressLine1 = models.CharField(max_length=255, db_column='supAddressLine1')
    supAddressLine2 = models.CharField(max_length=255, db_column='supAddressLine2')
    supCity = models.CharField(max_length=100, db_column='supCity')
    supState = models.CharField(max_length=100, db_column='supState')
    supPostalCode = models.CharField(max_length=20, db_column='supPostalCode')
    supCountry = models.CharField(max_length=100, db_column='supCountry')

    def __str__(self):
        return self.supplier_name
    
    class Meta:
        db_table = "tblSuppliers"
        managed = False
