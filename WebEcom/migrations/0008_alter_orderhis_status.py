# Generated by Django 3.2.6 on 2023-12-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebEcom', '0007_orderhis_t7'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhis',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
