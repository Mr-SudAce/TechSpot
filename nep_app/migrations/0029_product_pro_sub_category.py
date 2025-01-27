# Generated by Django 5.1 on 2024-09-12 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0028_remove_product_pro_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_sub_category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productSubCategory', to='nep_app.sub_category'),
        ),
    ]
