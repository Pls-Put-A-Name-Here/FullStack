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
# class CustomerTable(models.Model):
#     user_id = models.ForeignKey(UserTable, on_delete=models.CASCADE)
#     address_id = models.ForeignKey(UserAddressTable, on_delete=models.CASCADE)
# class BrandsTable(models.Model):
#     brand_name = models.CharField(max_length=100, null=False, blank=False)
#     country_of_origin = models.CharField(max_length=100)
#     year_established = models.IntegerField()
#     description = models.TextField()
#     created_date = models.DateField(auto_now_add=True)
#     last_edit_date = models.DateField(auto_now=True)
#     def __str__(self):
#         return self.brand_name
# class ProductCategoryTable(models.Model):
#     category = models.CharField(max_length=100, null=False)
#     created_date = models.DateTimeField(auto_now=True)
#     last_edited_date = models.DateTimeField(auto_now=True)
# Bright ends

# Kirk Starts
# Note: Django automatically creates an id (primary key) field unless specified otherwise
# This is the model for tblProductsSubCategory
# class ProductSubCategory(models.Model):
#     id = models.AutoField(primary_key=True,db_column='sctgIdpk')
#     subcategory_name = models.CharField(max_length=100, null=False, blank=False, unique=True,db_column='sctgName')
#     created_date = models.DateTimeField(auto_now_add=True,db_column='sctgCreatedDate')
#     last_edit_date = models.DateTimeField(auto_now=True,db_column='sctgLastEditDate')

# This is the model for tblProducts
# remove unnecessary qualifications example Product.product_name
# making it Product.name
# class Product(models.Model):
#     id = models.AutoField(primary_key=True,db_column='prdIdpk')
#     brand_id = models.ForeignKey('Brand', on_delete=models.CASCADE,db_column='prdBrdIdfk')
#     category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE,db_column='prdCtgIdfk')
#     subcategory_id = models.ForeignKey('ProductSubCategory', on_delete=models.CASCADE,db_column='prdSCtgIdfk')
#     name = models.CharField(max_length=255, null=False, blank=False,db_column='prdName')
#     description = models.TextField(db_column='prdDescription')
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2,db_column='prdUnitPrice')
#     stock_quantity = models.IntegerField(db_column='prdStockQuantity')
#     created_date = models.DateTimeField(auto_now_add=True,db_column='prdCreatedDate')
#     last_edit_date = models.DateTimeField(auto_now=True,db_column='prdLastEditDate')

# This is the model for tblProductImages
# class ProductImage(models.Model):
#     id = models.AutoField(primary_key=True,db_column='imgIdpk')
#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE,db_column='imgPrdIdfk')
#     url = models.URLField(db_column='imgURL')
#     descriptioin = models.TextField(db_column='imgDescription')
#     #consider using imagefield instead of urlfield
#     #consider using django's built in imagefield
#     image = models.ImageField(upload_to='product_images/',db_column='imgURL')
#     upload_date = models.DateTimeField(auto_now_add=True,db_column='imgUploadDate')
#     last_edit_date = models.DateTimeField(auto_now=True,db_column='imgLastEditDate')

# This is the model for tblProductDetails
# class ProductDetails(models.Model):
#     id = models.AutoField(primary_key=True,db_column='prdDetailsIdpk')
#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE,db_column='prdDetailsPrdIdfk')
#     weight = models.DecimalField(max_digits=10, decimal_places=2,db_column='prdWeight')
#     length = models.DecimalField(max_digits=10, decimal_places=2,db_column='prdLength')
#     width = models.CharField(db_column='prdWidth')
#     height = models.CharField(db_column='prdHeight')
#     dimensions = models.CharField(max_length=255,db_column='prdDimensions')
#     techinical_specifications = models.TextField(db_column='prdTechnicalSpecifications')
#     created_date = models.DateTimeField(auto_now_add=True,db_column='prdCreatedDate')
#     last_edit_date = models.DateTimeField(auto_now=True,db_column='prdLastEditDate')

# # This is the model for tblProductVariants
# class ProductVariant(models.Model):
#     id = models.AutoField(primary_key=True,db_column='prvIdpk')
#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE,db_column='prvPrdIdfk')
#     prvColor = models.CharField(max_length=100, null=False, blank=False,db_column='prvColor')
#     prvSize = models.CharField(max_length=100, null=False, blank=False,db_column='prvSize')
#     prvMaterial = models.CharField(max_length=100, null=False, blank=False,db_column='prvMaterial')
#     prvPriceModifier = models.DecimalField(max_digits=10, decimal_places=2,db_column='prvPriceModifier')
#     prvQuantityAvailable = models.IntegerField(db_column='prvQuantityAvailable')
#     prvSKU = models.CharField(max_length=100, null=False, blank=False, unique=True,db_column='prvSKU')
#     created_date = models.DateTimeField(auto_now_add=True,db_column='prvCreatedDate')
#     last_edit_date = models.DateTimeField(auto_now=True,db_column='prvLastEditDate')

# Kirk ends

# Joseph starts
# # This is the model for Order status table
# class OrderStatusTable(models.Model):
#     order_status_name = models.CharField(max_length=50)
#     order_status_description = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     last_edited_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.order_status_name


# This is the model for Status table
class PaymentStatus(models.Model):
    status_name = models.CharField(max_length=50)
    status_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_name


# This is the model for Order table
# class OrderTable(models.Model):
#     order_customer_id = models.ForeignKey(CustomerTable, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     order_delivery_address = models.CharField(max_length=255)
#     order_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
#     order_status = models.ForeignKey(OrderStatusTable, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     last_edited_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.order_customer_id)

# # This is the model for Order Items table
# class OrderItemsTable(models.Model):
#     order_id = models.ForeignKey(OrderTable, on_delete=models.CASCADE)
#     product_id = models.ForeignKey('ProductTable', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_date = models.DateTimeField(auto_now_add=True)
#     last_edited_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.order_id)

# # This is the model for supplier table
# class SupplierTable(models.Model):
#     supplier_name = models.CharField(max_length=100, null=False)
#     supplier_contact_info = models.CharField(max_length=255)
#     supplier_address_line1 = models.CharField(max_length=255)
#     supplier_address_line2 = models.CharField(max_length=255)
#     supplier_city = models.CharField(max_length=100)
#     supplier_state = models.CharField(max_length=100)
#     supplier_postal_code = models.CharField(max_length=20)
#     supplier_country = models.CharField(max_length=100)

#     def __str__(self):
#         return self.supplier_name
# Joseph ends
# Jonathan starts

# This the model for tb1Inventory
# class Inventory(models.Model):
#     invIdpk = models.AutoField(primary_key=True)
#     invPrdIdfk = models.ForeignKey('product.Product', on_delete=models.CASCADE)
#     invQuantityAvailable = models.IntegerField()
#     invUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     invUnitCost = models.DecimalField(max_digits=10, decimal_places=2)
#     invSupIdfk = models.ForeignKey('supplier.SupplierTable', on_delete=models.CASCADE)
#     invDateAdded = models.DateTimeField()
#     invExpirationDate = models.DateTimeField()
#     invLastUpdateDate = models.DateTimeField(auto_now=True)


# This the models for tblPaymentMethods
class PaymentMethod(models.Model):
    pmtIdpk = models.AutoField(primary_key=True)
    pmtName = models.CharField(max_length=100)
    pmtDescription = models.CharField(max_length=255)
    pmtCreatedDate = models.DateTimeField(auto_now_add=True)
    pmtLastUpdateDate = models.DateTimeField(auto_now=True)


# This the models for    tblPurchase


class Purchase(models.Model):
    pchIdpk = models.AutoField(primary_key=True)
    pchCustIdfk = models.ForeignKey("customer.CustomerTable", on_delete=models.CASCADE)
    pchPurchaseDate = models.DateTimeField()
    pchTotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    pchPmtIdfk = models.ForeignKey("PaymentMethod", on_delete=models.CASCADE)
    pchPstIdfk = models.ForeignKey("PaymentStatus", on_delete=models.CASCADE)
    pchCreatedDate = models.DateTimeField(auto_now_add=True)
    pchLastUpdateDate = models.DateTimeField(auto_now=True)


# This the models for tblCarts
# class Cart(models.Model):
#     crtIdpk = models.AutoField(primary_key=True)
#     crtCustomerIdfk = models.ForeignKey('Customer', on_delete=models.CASCADE)
#     crtCreatedAt = models.DateTimeField(auto_now_add=True)
#     crtStatus = models.CharField(max_length=50, default='Active')

# #This the models for tblCartItems
# class CartItem(models.Model):
#     crtItemIdpk = models.AutoField(primary_key=True)
#     crtItemCrtIdfk = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     crtItemPrdIdfk = models.ForeignKey('Product', on_delete=models.CASCADE)
#     crtItemQuantity = models.IntegerField()
#     crtItemUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

# -- Jonathan Ends
