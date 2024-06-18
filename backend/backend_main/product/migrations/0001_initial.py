# Generated by Django 4.0 on 2024-05-21 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(max_length=100)),
                ("country_of_origin", models.CharField(max_length=100)),
                ("year_established", models.IntegerField()),
                ("description", models.TextField()),
                ("created_date", models.DateField(auto_now_add=True)),
                ("last_edit_date", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "tblBrand",
            },
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=100)),
                ("created_date", models.DateTimeField(auto_now=True)),
                ("last_edited_date", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "tblProductCategory",
            },
        ),
        migrations.CreateModel(
            name="ProductSubCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="sctgIdpk", primary_key=True, serialize=False
                    ),
                ),
                (
                    "subcategory_name",
                    models.CharField(db_column="sctgName", max_length=100, unique=True),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, db_column="sctgCreatedDate"
                    ),
                ),
                (
                    "last_edit_date",
                    models.DateTimeField(auto_now=True, db_column="sctgLastEditDate"),
                ),
            ],
            options={
                "db_table": "tblProductSubCategory",
            },
        ),
        # migrations.CreateModel(
        #     name='Product',
        #     fields=[
        #         ('id', models.AutoField(db_column='prdIdpk', primary_key=True, serialize=False)),
        #         ('name', models.CharField(db_column='prdName', max_length=255)),
        #         ('description', models.TextField(db_column='prdDescription')),
        #         ('unit_price', models.DecimalField(db_column='prdUnitPrice', decimal_places=2, max_digits=10)),
        #         ('stock_quantity', models.IntegerField(db_column='prdStockQuantity')),
        #         ('created_date', models.DateTimeField(auto_now_add=True, db_column='prdCreatedDate')),
        #         ('last_edit_date', models.DateTimeField(auto_now=True, db_column='prdLastEditDate')),
        #         ('brand_id', models.ForeignKey(db_column='prdBrdIdfk', on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
        #         ('category_id', models.ForeignKey(db_column='prdCtgIdfk', on_delete=django.db.models.deletion.CASCADE, to='product.productcategory')),
        #         ('subcategory_id', models.ForeignKey(db_column='prdSCtgIdfk', on_delete=django.db.models.deletion.CASCADE, to='product.productsubcategory')),
        #     ],
        #     options={
        #         'db_table': 'tblProducts',
        #     },
        # ),
    ]
