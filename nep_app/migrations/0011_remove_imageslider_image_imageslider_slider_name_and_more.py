# Generated by Django 5.1 on 2024-09-03 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nep_app', '0010_imageslider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageslider',
            name='image',
        ),
        migrations.AddField(
            model_name='imageslider',
            name='slider_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='static/images/default_images.png', upload_to='static/images/slider')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='nep_app.imageslider')),
            ],
        ),
    ]
