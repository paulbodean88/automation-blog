from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^$', views.init_home, name='init_home'),
    url(r'^page/(?P<page_number>[0-9]*)', views.home_with_page, name='home_with_page'),
]

