from django.db import models

# Create your models here.
# Bright Start
# This is the model for tblUsers
class UserTable(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_email = models.CharField(max_lenght=50)
    user_date_of_birth = models.DateField()
    user_phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
# This is the model for tblAddresses
class UserAddressTable(models.Model):
    address_location = models.CharField(max_length=255)
    digital_address = models.CharField(max_length=255)
    house_address = models.CharField(max_length=255)
    def __str__(self):
        return self.digital_address
# This is the model for tblCustomers
class CustomerTable(models.Model):
    user_id = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    address_id = models.ForeignKey(UserAddressTable, on_delete=models.CASCADE)
class BrandsTable(models.Model):
    brand_name = models.CharField(max_length=100, null=False, blank=False)
    country_of_origin = models.CharField(max_length=100)
    year_established = models.IntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    last_edit_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.brand_name
class ProductCategoryTable(models.Model):
    category = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now=True)
    last_edited_date = models.DateTimeField(auto_now=True)
# Bright ends