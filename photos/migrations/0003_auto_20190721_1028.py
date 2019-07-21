# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-21 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_remove_image_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to='images/'),
        ),
    ]
