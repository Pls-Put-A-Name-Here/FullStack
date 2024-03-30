from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100, null=False, blank=False)
    country_of_origin = models.CharField(max_length=100)
    year_established = models.IntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    last_edit_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.brand_name
    
    class Meta:
        db_table="tblBrand"
    
class ProductCategory(models.Model):
    category = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now=True)
    last_edited_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="tblProductCategory"

class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True,db_column='sctgIdpk')
    subcategory_name = models.CharField(max_length=100, null=False, blank=False, unique=True,db_column='sctgName')
    created_date = models.DateTimeField(auto_now_add=True,db_column='sctgCreatedDate')
    last_edit_date = models.DateTimeField(auto_now=True,db_column='sctgLastEditDate')

    class Meta:
            db_table="tblProductSubCategory"   
class Product(models.Model):
    id = models.AutoField(primary_key=True,db_column='prdIdpk')
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE,db_column='prdBrdIdfk')
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,db_column='prdCtgIdfk')
    subcategory_id = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE,db_column='prdSCtgIdfk')
    name = models.CharField(max_length=255, null=False, blank=False,db_column='prdName')
    description = models.TextField(db_column='prdDescription')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,db_column='prdUnitPrice')
    stock_quantity = models.IntegerField(db_column='prdStockQuantity')
    created_date = models.DateTimeField(auto_now_add=True,db_column='prdCreatedDate')
    last_edit_date = models.DateTimeField(auto_now=True,db_column='prdLastEditDate')
    
    class Meta:
        db_table="tblProducts"