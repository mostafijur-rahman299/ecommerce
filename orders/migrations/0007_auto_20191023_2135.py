# Generated by Django 2.2.6 on 2019-10-23 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191023_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-timestamp']},
        ),
    ]
