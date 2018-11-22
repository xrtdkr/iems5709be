# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productions',
            name='Image',
            field=models.FileField(upload_to=b'/upload/pic/', blank=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='productions',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
