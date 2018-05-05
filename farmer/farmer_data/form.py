from django import forms
from .models import FarmerData


class CreateFarmerData(forms.ModelForm):
    sowing_date = forms.DateField(widget=forms.SelectDateWidget)
    crop_grown = forms.CharField(required=False)
    days_after_sowing = forms.IntegerField(required=False)
    fertiliser = forms.CharField(required=False)
    quantity = forms.IntegerField(required=False)
    price_unit = forms.IntegerField(required=False)


    class Meta:
        model = FarmerData
        fields = [
            "name",
            "phone",
            "language",
            "area",
            "village",
            "crop_grown",
            "sowing_date",
            "days_after_sowing",
            "days_from_sowing",
            "fertiliser",
            "quantity",
            "quantity_unit",
            "price_unit",
            # "bill",
        ]