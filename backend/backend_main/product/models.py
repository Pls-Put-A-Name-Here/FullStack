from django.db import models


# Create your models here.


class Brand(models.Model):
    brdIdpk = models.AutoField(primary_key=True, db_column="brdIdpk")
    brdName = models.CharField(
        max_length=100, null=False, blank=False, db_column="brdName"
    )
    brdCountryOfOrigin = models.CharField(
        max_length=100, db_column="brdCountryOfOrigin"
    )
    brdYearEstablished = models.IntegerField(db_column="brdYearEstablished")
    brdDescription = models.TextField(db_column="brdDescription")
    brdCreatedDate = models.DateField(auto_now_add=True, db_column="brdCreatedDate")
    brdLastEditDate = models.DateField(auto_now=True, db_column="brdLastEditDate")

    def __str__(self):
        return self.brdName

    class Meta:
        db_table = "tblBrands"
        managed = False


class ProductCategory(models.Model):
    ctgIdpk = models.AutoField(primary_key=True, db_column="ctgIdpk")
    ctgName = models.CharField(max_length=100, null=False, db_column="ctgName")
    ctgCreatedDate = models.DateTimeField(auto_now=True, db_column="ctgCreatedDate")
    ctgLastEditDate = models.DateTimeField(auto_now=True, db_column="ctgLastEditDate")

    class Meta:
        db_table = "tblProductCategories"
        managed = False


# Note: Django automatically creates an id (primary key) field unless specified otherwise
# This is the model for tblProductsSubCategory
class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column="sctgIdpk")
    subcategory_name = models.CharField(
        max_length=100, null=False, blank=False, unique=True, db_column="sctgName"
    )
    created_date = models.DateTimeField(auto_now_add=True, db_column="sctgCreatedDate")
    last_edit_date = models.DateTimeField(auto_now=True, db_column="sctgLastEditDate")

    def __str__(self):
        return self.subcategory_name

    class Meta:
        db_table = "tblProductSubCategories"
        managed = False


# This is the model for tblProducts
class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column="prdIdpk")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column="prdBrdIdfk")
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, db_column="prdCtgIdfk"
    )
    subcategory = models.ForeignKey(
        ProductSubCategory, on_delete=models.CASCADE, db_column="prdSCtgIdfk"
    )
    name = models.CharField(
        max_length=255, null=False, blank=False, db_column="prdName"
    )
    description = models.TextField(db_column="prdDescription")
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="prdUnitPrice"
    )
    stock_quantity = models.IntegerField(db_column="prdStockQuantity")
    created_date = models.DateTimeField(auto_now_add=True, db_column="prdCreatedDate")
    last_edit_date = models.DateTimeField(auto_now=True, db_column="prdLastEditDate")

    class Meta:
        db_table = "tblProducts"
        managed = False


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True, db_column="imgIdpk")
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="imgPrdIdfk"
    )
    url = models.URLField(db_column="imgURL")
    description = models.TextField(db_column="imgDescription")
    # consider using imagefield instead of urlfield
    # consider using django's built in imagefield
    # image = models.ImageField(upload_to='product_images/',db_column='imgURL')
    upload_date = models.DateTimeField(auto_now_add=True, db_column="imgUploadDate")
    last_edit_date = models.DateTimeField(auto_now=True, db_column="imgLastEditDate")

    class Meta:
        db_table = "tblProductImages"
        managed = False


# This is the model for tblProductVariants
class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True, db_column="prvIdpk")
    product_id = models.ForeignKey(
        "Product", on_delete=models.CASCADE, db_column="prvPrdIdfk"
    )
    prvColor = models.CharField(
        max_length=100, null=False, blank=False, db_column="prvColor"
    )
    prvSize = models.CharField(
        max_length=100, null=False, blank=False, db_column="prvSize"
    )
    prvMaterial = models.CharField(
        max_length=100, null=False, blank=False, db_column="prvMaterial"
    )
    prvPriceModifier = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="prvPriceModifier"
    )
    prvQuantityAvailable = models.IntegerField(db_column="prvQuantityAvailable")
    prvSKU = models.CharField(
        max_length=100, null=False, blank=False, unique=True, db_column="prvSKU"
    )
    created_date = models.DateTimeField(auto_now_add=True, db_column="prvCreatedDate")
    last_edit_date = models.DateTimeField(auto_now=True, db_column="prvLastEditDate")

    class Meta:
        db_table = "tblProductVariants"
        managed = False


# This is the model for tblProductDetails


class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True, db_column="prdDetailsIdpk")
    product_id = models.ForeignKey(
        "Product", on_delete=models.CASCADE, db_column="prdDetailsPrdIdfk"
    )
    weight = models.DecimalField(max_digits=10, decimal_places=2, db_column="prdWeight")
    length = models.DecimalField(max_digits=10, decimal_places=2, db_column="prdLength")
    # made change here : added max_length=255
    width = models.CharField(db_column="prdWidth", max_length=255)
    # made change here : added max_length=255
    height = models.CharField(db_column="prdHeight", max_length=255)
    dimensions = models.CharField(max_length=255, db_column="prdDimensions")
    techinical_specifications = models.TextField(db_column="prdTechnicalSpecifications")
    created_date = models.DateTimeField(auto_now_add=True, db_column="prdCreatedDate")
    last_edit_date = models.DateTimeField(auto_now=True, db_column="prdLastEditDate")

    class Meta:
        db_table = "tblProductDetails"
        managed = False
