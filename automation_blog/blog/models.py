from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
