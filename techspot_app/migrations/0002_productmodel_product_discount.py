# Generated by Django 5.2.1 on 2025-05-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techspot_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_discount',
            field=models.IntegerField(default=0),
        ),
    ]
