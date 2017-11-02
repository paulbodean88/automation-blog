from typing import List

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Post


def index(request):
    data = {
        'my_data': 'First post'
    }
    template = loader.get_template('articles/index.html')
    return HttpResponse(template.render(data, request))


def home(request, page=None):
    print(type(page))
    page = 0 if page is None else int(page[1:])
    posts = Post.objects.all().order_by("-created_date")

    render_posts = []
    for post in posts[page * 3: page * 3 + 3]:
        render_posts.append({
                'tile': post.title,
                'body': post.body
            })

    next_page_index = page + 1
    if page * 3 + 3 >= len(posts):
        next_page_index = -1

    response = {
        'posts': render_posts,
        'next_page': next_page_index,
        'prev_page': page - 1
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(response))
