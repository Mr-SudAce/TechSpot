# Generated by Django 5.2.1 on 2025-06-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techspot_app', '0008_productmodel_created_at_productmodel_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]
