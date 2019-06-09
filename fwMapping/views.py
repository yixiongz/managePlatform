from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from fwMapping import modelSer
from fwMapping import models
# 导入公共的函数
from fwMapping.public.generics import GetRespose, listView
from fwMapping.public.generics import GenericView
from fwMapping.public.mixins import CreateChangeView, DeleteView


class Fwchange(CreateChangeView, APIView):
    queryset = models.Mapping
    serializers_class = modelSer.MappingForm

    # 修改，新增主页
    def get(self, request, *args, **kwargs):
        mid = self.get_mid(request)
        if mid:
            forms = self.serializers_class(instance=mid)
            return render(request, "change.html", {"forms": forms, "queryset": mid})
        else:
            forms = self.serializers_class()
            return render(request, "add.html", {"forms": forms})


class IndexDetail(ViewSetMixin, DeleteView):
    queryset = models.Mapping
    serializers_class = modelSer.MappingForm

    def list(self, request, *args, **kwargs):
        get_list = listView(request, self.queryset, self.serializers_class)
        return render(request, 'indexDetail.html', get_list)


class LanDetail(ViewSetMixin, DeleteView):
    queryset = models.Laninter
    serializers_class = modelSer.LanForm

    def list(self, request, *args, **kwargs):
        get_list = listView(request, self.queryset, self.serializers_class)
        return render(request, 'LanDetail.html', get_list)


class Lanchange(CreateChangeView):
    queryset = models.Laninter
    serializers_class = modelSer.LanForm

    # 修改，新增主页
    def get(self, request, *args, **kwargs):
        mid = self.get_mid(request)
        if mid:
            forms = self.serializers_class(instance=mid)
            return render(request, "lanchange.html", {"forms": forms, "queryset": mid})
        else:
            forms = self.serializers_class()
            return render(request, "lanadd.html", {"forms": forms})

