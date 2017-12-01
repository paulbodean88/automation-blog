from django.http import HttpResponse
from django.template import loader

from .controllers.post_controller import PostController


def index(request):
    data = {
        'my_data': 'First post'
    }
    template = loader.get_template('articles/index.html')
    return HttpResponse(template.render(data, request))


def init_home(request):
    render_posts = []
    for post in PostController.get_page(0):
        print(post.title)
        render_posts.append({
            'title': post.title,
            'summary': post.summary,
            'author': post.author.username,
            'created': post.created_date
        })

    response = {
        'posts': render_posts,
        'next_page': 1 if PostController.has_next_page(0) else -1,
        'current_page': 0,
        'prev_page': -1
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(response))


def home_with_page(request, page_number=None):

    page = 0 if page_number is None else int(page_number)

    render_posts = []
    for post in PostController.get_page(page):
        print(post.title)
        render_posts.append({
            'title': post.title,
            'summary': post.summary,
            'author': post.author.username,
            'created': post.created_date
            })

    response = {
        'posts': render_posts,
        'next_page': page + 1 if PostController.has_next_page(page) else -1,
        'current_page': page,
        'prev_page': page - 1
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(response))
