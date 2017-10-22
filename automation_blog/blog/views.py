from django.http import HttpResponse
from django.template import loader

from .models import Article


def index(request):
    all_articles = Article.objects.all()
    template = loader.get_template('articles/index.html')
    context = {
        'all_articles': all_articles,
    }

    return HttpResponse(template.render(context, request))


def detail(request, article):
    return HttpResponse('<h2>Details for article id: ' + str(article) + '</h2>')
