from django.db import models
from core.models import User,Address

# Create your models here.
# This is the model for tblCustomers
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True,db_column='custIdpk')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column='custUsrIdfk')
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE,db_column='custAdrIdfk')
    
    class Meta:
        db_table='tblCustomers'
        managed=False