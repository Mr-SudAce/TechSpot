# Generated by Django 5.1 on 2024-09-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0016_alter_image_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_slider',
            name='image',
            field=models.ImageField(upload_to='images/slider/'),
        ),
    ]
