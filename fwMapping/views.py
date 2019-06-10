from fwMapping import modelSer
from fwMapping import models
# 导入公共的函数
from fwMapping.public.mixins import CreateChangeView, ListDeleteView


class Fwchange(CreateChangeView):
    queryset = models.Mapping
    serializers_class = modelSer.MappingForm


class IndexDetail(ListDeleteView):
    queryset = models.Mapping
    serializers_class = modelSer.MappingForm
    render_html = "indexDetail.html"
    page_num = 5


class LanDetail(ListDeleteView):
    queryset = models.Laninter
    serializers_class = modelSer.LanForm
    render_html = "LanDetail.html"
    page_num = 5


class Lanchange(CreateChangeView):
    queryset = models.Laninter
    serializers_class = modelSer.LanForm


class WanDetail(ListDeleteView):
    queryset = models.Waninter
    serializers_class = modelSer.WanForm
    render_html = "wanDetail.html"
    page_num = 5


class Wanchange(CreateChangeView):
    queryset = models.Waninter
    serializers_class = modelSer.WanForm
