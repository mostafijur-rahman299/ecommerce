# Generated by Django 2.2.3 on 2019-09-20 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_subcategory'),
        ('products', '0012_auto_20190904_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
    ]
