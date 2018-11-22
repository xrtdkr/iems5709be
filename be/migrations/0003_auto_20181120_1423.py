# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be', '0002_auto_20181030_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionInShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('production_id', models.IntegerField(default=-1)),
                ('shopping_cart_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=-1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=50)),
                ('nickname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=1000)),
                ('session_id', models.CharField(max_length=1000, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='create_time',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='series',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='state',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='bill',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='productioninbill',
            name='bill_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='productioninbill',
            name='production_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='productions',
            name='Image',
            field=models.FileField(upload_to=b'./static/upload/pic/', blank=True),
        ),
    ]
