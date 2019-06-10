# coding:utf-8
#
import json
from django.shortcuts import redirect, reverse
from fwMapping.public.paginators import Paginator_page
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse

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


def listView(request, queryset, serializers_class):
    # 使用ID进行排序
    queryset = queryset.objects.all().order_by('pk')
    # 分页器 request 将对象传入分层器， queryset将数据对象传入， page_num显示多少行
    page_num = 10
    p = Paginator_page(request, queryset, page_num)
    get_list = p.get_page

    forms = serializers_class(request.POST)
    get_list["forms"] = forms
    return get_list


class GenericView(APIView):
    '''
    :param request:  request 中携带过来的数据
    :param queryset:  models.表, 传递过来的表
    :param serializers_class: 序列化对象
    :return:
    '''

    queryset = None
    serializers_class = None
    render_html = None
    page_num = 10

    def get_mid(self, request, *args, **kwargs):
        mid = request.GET.get("changeID")
        # 判断如果为空就直接返回forms执行add， post方法
        # 如果它不是一个整形, changeID那就直接判断为空,
        if mid:
            try:
                if isinstance(int(mid), int):
                    queryset = self.queryset.objects.get(pk=mid)
                    return queryset
            except Exception:
                return None
        # 啥都没的话就直接返回None
        return None

    # 主页， 以及分页
    def listView(self, request, *args, **kwargs):
        # 使用ID进行排序
        queryset = self.queryset.objects.all().order_by('pk')
        # 分页器 request 将对象传入分层器， queryset将数据对象传入， page_num显示多少行
        p = Paginator_page(request, queryset, self.page_num)
        get_list = p.get_page

        forms = self.serializers_class(request.POST)
        get_list["forms"] = forms
        return render(request, self.render_html, get_list)

    # 修改添加的index页面,
    def getView(self, request, *args, **kwargs):
        mid = self.get_mid(request)
        if mid:
            forms = self.serializers_class(instance=mid)
            return render(request, "change.html", {"forms": forms, "queryset": mid})
        else:
            forms = self.serializers_class()
            return render(request, "add.html", {"forms": forms})

    # 添加映射页面
    def postView(self, request, *args, **kwargs):
        # print(request.path)  # 获取url路径
        forms = self.serializers_class(request.POST)
        return JsonResponse(self.save(forms))

    # 修改映射页面
    def putView(self, request, *args, **kwargs):
        # querySet 转换成字典
        request_dir = request.data.dict()
        # 删除id并返回它的结果用于查询， 然后就继续执行下边的代码
        mid = request_dir.pop("id")
        queryset = self.queryset.objects.filter(pk=mid).first()
        forms = self.serializers_class(request_dir, instance=queryset)
        # 如果检验成功直接保存, 并返回10000
        return JsonResponse(self.save(forms))

    # 删除
    def deleteView(self, request, queryset):
        mid = json.loads(request.body).get("mid")
        try:
            # 将表传递过来， 注意如果导入的是 models 那就传入 models.表名
            res = queryset.objects.filter(pk=mid)
            # 如果删除成功 response.status= 10000 否则就等于10001
            status = 10000 if res.delete() else 10001
        except Exception:
            status = 10001
        # 最终将字典返回, 成功的返回状态10000， 失败返回10001
        return status

    # 修改，添加 form保存
    def save(self, forms, *args, **kwargs):
        # 如果检验成功直接保存, 并返回10000
        try:
            if forms.is_valid():
                forms.save()
                return {"status": 10000}
            else:
                msg = forms.errors.get_json_data()
                return {"status": 10001, "msg": msg}
        except Exception:
            return {"status": 10002, "msg":{"__all__": [{"message": "添加失败"}]}}
