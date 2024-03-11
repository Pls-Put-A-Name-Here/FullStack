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


#vine start
class SupplierTable(models.Model):
    supplier = models.CharField(max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now=True)
    last_edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self

class CartTable(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Link to User model
    # ... other fields (optional)
    created_date = models.DateTimeField(auto_now=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for user: {self.user.username}"

class CartItemTable(models.Model):
  cart = models.ForeignKey(CartTable, on_delete=models.CASCADE)  # Link to Cart model
  product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  # Link to Product Model (assuming it exists)
  quantity = models.PositiveIntegerField()
  created_date = models.DateTimeField(auto_now=True)
  last_edited_date = models.DateTimeField(auto_now=True)

  def get_total_price(self):
    # Implement logic to calculate total price (quantity * product.price)
    return self.quantity * self.product.price  # Assuming a product.price field

  def __str__(self):
    return f"{self.quantity}x {self.product.name} (cart: {self.cart.id})"

class ReviewsTable(models.Model):
  product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  # Link to Product Model
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)  # Optional user field
  review = models.TextField()  # Allow longer reviews
  rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)  # Optional rating
  title = models.CharField(max_length=100, null=True, blank=True)  # Optional title
  created_date = models.DateTimeField(auto_now=True)
  last_edited_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    if self.title:
      return f"{self.title} - Review by {self.user.username if self.user else 'Anonymous'}"
    else:
      return f"Review by {self.user.username if self.user else 'Anonymous'}"


#vine ends