from django.contrib import admin
from .models import Post, Category, Tag, Image, Section


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'article_id')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'section_id')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Section, SectionAdmin)
