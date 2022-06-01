from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^prestamo/$', views.JSONResponse.prestamo_list),
    re_path(r'^prestamo/(?P<pk>[0-9]+)/$', views.JSONResponse.prestamo_detail),

]