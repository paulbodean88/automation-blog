from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    # url(r'^home', views.home, name='index1'),
    url(r'^home(/[0-9]*)+/', views.home, name='home'),
]

