from fwMapping.public.generics import GenericView
from fwMapping.public.generics import GetRespose
from django.http import JsonResponse


# 新增修改类, 直接运行putView, 跟postView
class CreateChangeView(GenericView):
    # 修改数据
    def put(self, request, *args, **kwargs):
        return JsonResponse(self.putView(request))

    # 新增
    def post(self, request, *args, **kwargs):
        return JsonResponse(self.postView(request))


class DeleteView(GenericView):
    def delete(self, request, *args, **kwargs):
        response = GetRespose()
        response.status = self.deleteView(request, self.queryset)
        return JsonResponse(response.get_dic)
