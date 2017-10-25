from django.db import models
from django.utils.datetime_safe import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now, blank=True)
    updated = models.DateField(default=datetime.now, blank=True)
    category_id = models.ForeignKey(Category, null=True)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=3000)
    article_id = models.ForeignKey(Article)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=100)
    data = models.BinaryField()
    section_id = models.ForeignKey(Section)

    def __str__(self):
        return self.name
