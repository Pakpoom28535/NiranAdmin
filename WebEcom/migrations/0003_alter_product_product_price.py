# Generated by Django 3.2.6 on 2023-11-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebEcom', '0002_alter_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Price',
            field=models.IntegerField(),
        ),
    ]
