from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Category name', max_length=100)
    description = models.CharField('Category description', max_length=255, default='unknown category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Define the blog_post table
    """
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    summary = models.TextField(max_length=1000, default='unknown summary')

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=3000)
    article_id = models.ForeignKey(Post)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=100)
    data = models.BinaryField()
    section_id = models.ForeignKey(Section)

    def __str__(self):
        return self.name
