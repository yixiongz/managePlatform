from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from fwMapping import modelSer
from fwMapping import models


# 公共返回字典
class GetRespose(object):
    '''
        10000: 返回成功
        10001: 参数错误
    '''

    def __init__(self):
        self.status = 10000
        self.msg = None

    @property
    def get_dic(self):
        return self.__dict__


def index(request):
    return render(request, 'index.html')


class FwindexShow(ViewSetMixin, APIView):
    def get(self, request, *args, **kwargs):
        mapping_list = models.Mapping.objects.all()
        forms = modelSer.MappingForm()
        return render(request, 'fwmappIndex.html', {"forms": forms, "mapping_list": mapping_list})


# class FwmappAdd(APIView)
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


def fwchange(request, mid, *args, **kwargs):
    print(mid)
    response = GetRespose()
    map_list = models.Mapping.objects.filter(mapid=mid).first()
    if request.method == "GET":
        forms = modelSer.MappingForm(instance=map_list)
        return render(request, "change.html", {"forms": forms})

    if request.method == "POST":
        forms = modelSer.MappingForm(request.POST, instance=map_list)
        print("forms: ", forms)
        # print(request.POST)
        if forms.is_valid():
            print("检验通过")
            forms.save()
        else:
            response.status = 10001
            data = forms.errors.get_json_data()
            response.msg = data
        return JsonResponse(response.get_dic)


def delete(request, *args, **kwargs):
    if request.method == "POST":
        response = GetRespose()
        res = models.Mapping.objects.filter(mapid=request.POST.get("mid"))
        response.status = 10000 if res.delete() else 10001
        return JsonResponse(response.get_dic)


def lanindex(request, *args, **kwargs):
    mapping_list = models.Laninter.objects.all()
    forms = modelSer.LanForm(request.POST)
    return render(request, 'lanIndex.html', {"forms": forms, "mapping_list": mapping_list})


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


def landelete(request, *args, **kwargs):
    if request.method == "POST":
        response = GetRespose()
        res = models.Laninter.objects.filter(id=request.POST.get("mid"))
        # 如果删除成功 response.status= 10000 否则就等于10001
        response.status = 10000 if res.delete() else 10001
        return JsonResponse(response.get_dic)


def lanchange(request, mid, *args, **kwargs):
    response = GetRespose()
    map_list = models.Laninter.objects.filter(id=mid).first()
    if request.method == "GET":
        forms = modelSer.LanForm(instance=map_list)
        return render(request, "lanchange.html", {"forms": forms, "map_list": map_list})

    if request.method == "POST":
        print(request.POST, map_list)
        forms = modelSer.LanForm(request.POST, instance=map_list)
        print("forms: ", forms)
        if forms.is_valid():
            print("检验通过")
            forms.save()
        else:
            response.status = 10001
            data = forms.errors.get_json_data()
            response.msg = data
        return JsonResponse(response.get_dic)
