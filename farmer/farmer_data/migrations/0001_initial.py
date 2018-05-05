# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-05 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('crop_grown', models.CharField(max_length=100)),
                ('sowing_date', models.DateField()),
                ('days_after_sowing', models.IntegerField(default=0)),
                ('fertiliser', models.CharField(max_length=100)),
                ('price_unit', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('quantity_unit', models.CharField(choices=[('kg', 'KG'), ('ton', 'TON'), ('g', 'G'), ('l', 'L'), ('ml', 'ML')], default='kg', max_length=3)),
                ('bill', models.PositiveIntegerField()),
            ],
        ),
    ]
