# Generated by Django 5.0.3 on 2024-07-14 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_alter_customertable_options"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="customertable",
            table="tblCustomers",
        ),
    ]
