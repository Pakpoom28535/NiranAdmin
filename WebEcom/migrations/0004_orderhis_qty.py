# Generated by Django 3.2.6 on 2023-12-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebEcom', '0003_orderhis'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhis',
            name='qty',
            field=models.IntegerField(null=True),
        ),
    ]
