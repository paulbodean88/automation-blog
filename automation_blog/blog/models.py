from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title
