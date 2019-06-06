#coding:utf-8
#
import json

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

def deleteView(request, modeltab):
    mid = json.loads(request.body).get("mid")
    try:
        # 将表传递过来， 注意如果导入的是 models 那就传入 models.表名
        res = modeltab.objects.filter(pk=mid)
        # 如果删除成功 response.status= 10000 否则就等于10001
        status = 10000 if res.delete() else 10001
    except Exception:
        status = 10001
    # 最终将字典返回, 成功的返回状态10000， 失败返回10001
    return status


def putView(request, modeltab, serializers):
    '''
    :param request:  request 中携带过来的数据
    :param modeltab:  models.表, 传递过来的表
    :param serializers: 序列化对象
    :return:
    '''
    # querySet 转换成字典
    request_dir = request.data.dict()
    # 删除id并返回它的结果用于查询， 然后就继续执行下边的代码
    mid = request_dir.pop("id")
    queryset = modeltab.objects.filter(id=mid).first()
    forms = serializers(request_dir, instance=queryset)
    # 如果检验成功直接保存, 并返回10000
    if forms.is_valid():
        forms.save()
        return {"status": 10000}
    else:
        msg = forms.errors.get_json_data()
        return {"status": 10001, "msg": msg}

