# Generated by Django 2.2.3 on 2019-09-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20190919_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
