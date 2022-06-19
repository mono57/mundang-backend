from django.contrib import admin
from django.http import QueryDict

from blog.models import Post, PostCategory, PostType, UserInvite
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


class UserInviteModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'verified']
    actions = ['send_invite_link']

    def send_invite_link(self, request, queryset):
        for q in queryset:
            q.send_invite_mail(request)

    send_invite_link.short_description = "Envoyer le lien d'invitation"

admin.site.register(UserInvite, UserInviteModelAdmin)
