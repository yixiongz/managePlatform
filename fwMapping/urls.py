from django.urls import path, include
from fwMapping import views


app_name = "fwMapping"
urlpatterns = [
    # path('index/', views.index, name="index"),
    path('indexdetail/', views.IndexDetail.as_view({'get': 'list', 'delete': 'delete'}), name="indexDetail"),
    path('add/', views.FwmapAdd, name="add"),
    path('change/', views.Fwchange.as_view(), name="change"),

    path('landetail/', views.LanDetail.as_view({'get': 'list', 'delete': 'delete'}), name="lanDetail"),
    # 添加或修改路由
    path('lanchange', views.Lanchange.as_view(), name="lanChange"),
]
