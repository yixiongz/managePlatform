from django.urls import path, include
from fwMapping import views


app_name = "fwMapping"
urlpatterns = [
    # path('index/', views.index, name="index"),
    path('index/', views.FwindexShow.as_view({'get': 'get'}), name="index"),
    path('add/', views.FwmapAdd, name="add"),
    path('change/<int:mid>', views.fwchange, name="change"),
    path('delete/', views.delete, name="delete"),
]
