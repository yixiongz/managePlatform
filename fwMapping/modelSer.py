# coding:utf-8
#
from django import forms
from fwMapping import models


class MappingForm(forms.ModelForm):
    class Meta:
        model = models.Mapping
        fields = "__all__"
