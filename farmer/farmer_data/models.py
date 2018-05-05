# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FarmerData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    language = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    crop_grown = models.CharField(max_length=100)
    sowing_date = models.DateField(auto_now=False, auto_now_add=False)
    days_after_sowing = models.IntegerField(default=0)
    days_from_sowing = models.IntegerField(default=0)
    fertiliser = models.CharField(max_length=100)
    quantity = models.IntegerField()

    qty_unit = (
        ('kg', 'KG'),
        ('ton', 'TON'),
        ('g', 'G'),
        ('l', 'L'),
        ('ml', 'ML')
    )
    quantity_unit = models.CharField(max_length=3, choices=qty_unit, default='kg')
    price_unit = models.IntegerField()
    bill = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# class FarmData(models.Model):
#     area = models.CharField(max_length=100)
#     village = models.CharField(max_length=100)
#     crop_grown = models.CharField(max_length=100)
#     sowing_date = models.DateTimeField(auto_now=False)
#
#
# class ScheduledData(models.Model):
#     days_after_sowing = models.IntegerField()
#     fertiliser = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#     qty_unit = (
#         ('kg', 'KG'),
#         ('ton', 'TON'),
#         ('g', 'G'),
#         ('l', 'L'),
#         ('ml', 'ML')
#     )
#     quantity_unit = models.CharField(max_length=3, choices=qty_unit)
