from django.db import models
from core.models import UserAddressTable, UserTable

# Create your models here.
# This is the model for tblCustomers
class CustomerTable(models.Model):
    custIdpk = models.AutoField(primary_key=True, db_column='custIdpk')
    custUsrIdfk = models.ForeignKey(UserTable, on_delete=models.CASCADE, db_column='custUsrIdfk')
    custAdrIdfk = models.ForeignKey(UserAddressTable, on_delete=models.CASCADE, db_column='custAdrIdfk')

    class Meta:
        db_table = "tblCustomers"
        managed = False