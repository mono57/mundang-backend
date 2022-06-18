from django.contrib import admin

from blog.models import Post, PostCategory, PostType
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'published_on']

admin.site.register(Post, PostModelAdmin)


class PostCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'badge_color']

admin.site.register(PostCategory, PostCategoryModelAdmin)


class PostTypeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']

admin.site.register(PostType, PostTypeModelAdmin)