from django.urls import path, include
from fwMapping import views


app_name = "fwMapping"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('test/', views.Test.as_view(), name="test"),
]
