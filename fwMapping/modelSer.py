# coding:utf-8
#
from django import forms
from fwMapping import models


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
