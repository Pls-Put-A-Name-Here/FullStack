# Generated by Django 5.0.3 on 2024-07-14 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_brand_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='brand',
            table='tblBrands',
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='tblProductCategories',
        ),
        migrations.AlterModelTable(
            name='productdetails',
            table='tblProductDetails',
        ),
        migrations.AlterModelTable(
            name='productimage',
            table='tblProductImages',
        ),
        migrations.AlterModelTable(
            name='productvariant',
            table='tblProductVariants',
        ),
    ]
