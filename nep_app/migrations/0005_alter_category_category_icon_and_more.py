# Generated by Django 5.1 on 2024-08-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0004_category_category_icon_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_icon',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
