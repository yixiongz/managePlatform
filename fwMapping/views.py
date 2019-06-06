from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from fwMapping import modelSer
from fwMapping import models
import json
from rest_framework.generics import GenericAPIView
# 导入公共的函数
from fwMapping.public.generics import GetRespose, deleteView, putView
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'index.html')


def FwmapAdd(request, *args, **kwargs):
    response = GetRespose()
    if request.method == "GET":
        forms = modelSer.MappingForm()
        return render(request, "add.html", {"forms": forms})
    elif request.method == "POST":
        print("FwmapAdd", request.POST)
        res = modelSer.MappingForm(request.POST)
        if res.is_valid():
            res.save()
        else:
            response.status = 10001
            data = res.errors.get_json_data()
            response.msg = data
        return JsonResponse(response.get_dic)


class Fwchange(APIView):
    def get(self, request, *args, **kwargs):
        mid = request.GET.get("changeID")
        queryset = models.Mapping.objects.filter(id=mid).first()
        forms = modelSer.MappingForm(instance=queryset)
        return render(request, "change.html", {"forms": forms, "queryset": queryset})

    def put(self, request, *args, **kwargs):
        ret = putView(request, models.Mapping, modelSer.MappingForm)
        return JsonResponse(ret)


class IndexDetail(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        queryset = models.Mapping.objects.all()
        forms = modelSer.MappingForm(request.POST)
        return render(request, 'indexDetail.html', {"forms": forms, "queryset": queryset})

    def delete(self, request, *args, **kwargs):
        response = GetRespose()
        response.status = deleteView(request, models.Mapping)
        return JsonResponse(response.get_dic)


class LanDetail(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        queryset = models.Laninter.objects.all()
        forms = modelSer.LanForm(request.POST)
        return render(request, 'LanDetail.html', {"forms": forms, "queryset": queryset})

    def delete(self, request, *args, **kwargs):
        response = GetRespose()
        response.status = deleteView(request, models.Laninter)
        return JsonResponse(response.get_dic)


def lanAdd(request, *args, **kwargs):
    response = GetRespose()
    if request.method == "GET":
        forms = modelSer.LanForm()
        return render(request, "lanadd.html", {"forms": forms})
    elif request.method == "POST":
        res = modelSer.LanForm(request.POST)
        if res.is_valid():
            res.save()
        else:
            response.status = 10001
            data = res.errors.get_json_data()
            response.msg = data
        return JsonResponse(response.get_dic)


class Lanchange(APIView):
    # 修改，新增主页
    def get(self, request, *args, **kwargs):
        mid = request.GET.get("changeID")
        response = GetRespose()
        if mid:
            # 如果值不存在就直接抛404错误
            queryset = get_object_or_404(models.Laninter, pk=mid)
            # queryset = models.Laninter.objects.filter(id=mid).first()
            forms = modelSer.LanForm(instance=queryset)
            return render(request, "lanchange.html", {"forms": forms, "queryset": queryset})
        forms = modelSer.LanForm()
        return render(request, "lanadd.html", {"forms": forms})


    # 修改数据
    def put(self, request, *args, **kwargs):
        ret = putView(request, models.Laninter, modelSer.LanForm)
        return JsonResponse(ret)

    # 新增
    def post(self, request, *args, **kwargs):
        response = GetRespose()
        res = modelSer.LanForm(request.POST)
        if res.is_valid():
            res.save()
        else:
            response.status = 10001
            data = res.errors.get_json_data()
            response.msg = data
        return JsonResponse(response.get_dic)
