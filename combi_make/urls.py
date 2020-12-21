from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ok', views.ok, name='ok'),
    path('no', views.no, name='no'),
    path('download', views.download, name='download'),
]