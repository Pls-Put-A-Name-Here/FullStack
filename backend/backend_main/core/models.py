from django.db import models


# Create your models here.
# Bright Start
# This is the model for tblUsers
class UserTable(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
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

# JoeWise Starts
# This is the model for Order status table
class OrderStatusTable(models.Model):
    order_status_name = models.CharField(max_length=50)
    order_status_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_status_name

# This is the model for Status table
class StatusTable(models.Model):
    status_name = models.CharField(max_length=50)
    status_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_name

# This is the model for Order table
class OrderTable(models.Model):
    order_customer_id = models.ForeignKey(CustomerTable, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_delivery_address = models.CharField(max_length=255)
    order_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey(OrderStatusTable, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order_customer_id)

# This is the model for Order Items table
class OrderItemsTable(models.Model):
    order_id = models.ForeignKey(OrderTable, on_delete=models.CASCADE)
    product_id = models.ForeignKey('ProductTable', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order_id)

# This is the model for supplier table
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
# JoeWise Ends