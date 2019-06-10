from django.urls import path, include
from fwMapping import views


app_name = "fwMapping"
urlpatterns = [
    # path('index/', views.index, name="index"),
    # path('indexdetail/', views.IndexDetail.as_view({'get': 'list', 'delete': 'delete'}), name="indexDetail"),
    path('indexdetail/', views.IndexDetail.as_view(), name="indexDetail"),
    path('change', views.Fwchange.as_view(), name="change"),

    path('landetail/', views.LanDetail.as_view(), name="lanDetail"),
    path('lanchange', views.Lanchange.as_view(), name="lanChange"),  # 添加或修改路由

    path('wandetail/', views.WanDetail.as_view(), name="wanDetail"),
    path('wanchange', views.Wanchange.as_view(), name="wanChange"),  # 添加或修改路由
]
