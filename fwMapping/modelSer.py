# coding:utf-8
#
from django import forms
from fwMapping import models
from rest_framework import serializers

from django.core.exceptions import ValidationError
from django.forms import Form


class MappingForm(forms.ModelForm):
    class Meta:
        model = models.Mapping
        fields = "__all__"

        labels = {
            "mapid": "ID",
            "serid": "序列号",
            "protocol": "协议",
            "lanip": "内网IP",
            "lanport": "内网端口",
            "wanip": "外网IP",
            "wanport": "外网端口",
        }
        widgets = {
            "mapid": forms.widgets.NumberInput(attrs={"class": "form-control"}),
            "serid": forms.widgets.NumberInput(attrs={"class": "form-control"}),
            "protocol": forms.widgets.Select(attrs={"class": "form-control"}),
            "lanip": forms.widgets.Select(attrs={"class": "form-control"}),
            "lanport": forms.widgets.NumberInput(attrs={"class": "form-control"}),
            "wanip": forms.widgets.Select(attrs={"class": "form-control"}),
            "wanport": forms.widgets.NumberInput(attrs={"class": "form-control"})
        }

        error_messages = {
            "mapid": {"required": "不能为空"},
            "serid": {"required": "不能为空"},
            "protocol": {"required": "不能为空"},
            "lanip": {"required": "不能为空"},
            "lanport": {"required": "不能为空"},
            "wanip": {"required": "不能为空"},
            "wanport": {"required": "不能为空"},
        }

    def clean_lanport(self):
        wanport = self.cleaned_data["lanport"]
        if wanport < 0 or wanport > 65535:
            raise ValidationError("端口范围0-65535")
        return self.cleaned_data["lanport"]

    def clean_wanport(self):
        wanport = self.cleaned_data["wanport"]
        if wanport < 0 or wanport > 65535:
            raise ValidationError("端口范围0-65535")
        return self.cleaned_data["wanport"]


class LanForm(MappingForm):
    class Meta:
        model = models.Laninter
        fields = "__all__"
        labels = {
            "lanip": "内网IP",
        }
        widgets = {
            "lanip": forms.widgets.TextInput(attrs={"class": "form-control"}),
        }

        error_messages = {
            "lanip": {"required": "不能为空"},
        }


class WanForm(MappingForm):
    class Meta:
        model = models.Waninter
        fields = "__all__"
        labels = {
            "wanip": "外网IP",
        }
        widgets = {
            "wanip": forms.widgets.TextInput(attrs={"class": "form-control"}),
        }

        error_messages = {
            "wanip": {"required": "不能为空"},
        }
