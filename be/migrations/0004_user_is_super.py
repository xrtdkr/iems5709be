# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be', '0003_auto_20181120_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_super',
            field=models.BooleanField(default=False),
        ),
    ]
