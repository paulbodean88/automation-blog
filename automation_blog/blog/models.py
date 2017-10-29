from django.db import models


class Author(models.Model):
    """
    Define the blog_author table
    """
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Category name', max_length=100)
    description = models.CharField('Category description', max_length=255, default='sal')

    class Meta:
        """
        Change the plural of the category, Django special class
        """
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
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
