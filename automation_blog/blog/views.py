from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    data = {
        'my_data': 'First post'
    }
    template = loader.get_template('articles/index.html')
    return HttpResponse(template.render(data, request))


def home(request):
    # template = loader.get_template('articles/home.html')
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
