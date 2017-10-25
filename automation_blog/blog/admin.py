from django.contrib import admin

from .models import Article, Section, Category, Image


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date', 'updated', 'summary', 'category_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'article_id']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Section)
admin.site.register(Image)
