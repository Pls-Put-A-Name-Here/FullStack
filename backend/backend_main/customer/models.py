from django.db import models
from core.models import *


# Create your models here.
# This is the model for tblCustomers
class CustomerTable(models.Model):
    user_id = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    address_id = models.ForeignKey(UserAddressTable, on_delete=models.CASCADE)
