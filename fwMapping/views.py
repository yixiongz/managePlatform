from django.shortcuts import render
from rest_framework.views import APIView
from fwMapping import modelSer
from fwMapping import models


def index(request):
    return render(request, 'index.html')


class Test(APIView):
    def get(self, request, *args, **kwargs):
        mapping_list = models.Mapping.objects.all()
        print(mapping_list)
        forms = modelSer.MappingForm()
        print(forms)
        return render(request, 'test.html', {"forms": forms, "mapping_list": mapping_list})