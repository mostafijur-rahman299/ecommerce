# Generated by Django 2.2.3 on 2019-09-03 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
