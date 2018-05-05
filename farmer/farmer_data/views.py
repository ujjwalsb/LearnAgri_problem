# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from .models import FarmerData
from .form import CreateFarmerData


def viewfarmerdata(request):
    queryset = FarmerData.objects.all()
    for obj in queryset:
        if obj.quantity_unit == 'g' or obj.quantity_unit == 'ml':
            obj.bill = obj.price_unit * (obj.quantity / 1000)
        elif obj.quantity_unit == 'ton':
            obj.bill = obj.price_unit * (obj.quantity * 1000)
        else:
            obj.bill = obj.price_unit * obj.quantity

    context = {
        "data_values": queryset,
        "title": "Farmer Data",
    }
    return render(request, "details.html", context)


def createfarmer(request):
    formvariable = CreateFarmerData(request.POST or None)
    if formvariable.is_valid():
        instance = formvariable.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/')
    context = {
        "title": "Create Farmer Data",
        "form": formvariable,
    }
    return render(request, "create.html", context)


def schedule(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    schedule_date = FarmerData.objects.filter(sowing_date__range=[today, tomorrow])

    context = {
        "data_values": schedule_date,
        "title": "Schedule Due for Today/Tomorrow",
    }
    return render(request, "schedule.html", context)


def growingcrop(request):
    crop_qs = FarmerData.objects.exclude(crop_grown__isnull=True).exclude(crop_grown__exact='')
    context = {
        "crop_values": crop_qs,
        "title": "Farmer Growing Crops"
    }
    return render(request, "cropgrown.html", context)



