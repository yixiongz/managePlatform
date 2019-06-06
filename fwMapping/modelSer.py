# coding:utf-8
#
from django import forms
from fwMapping import models
from rest_framework import serializers


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
