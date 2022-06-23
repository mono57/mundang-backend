from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import UserInvite

class UserInviteModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'verified']
    actions = ['send_invite_link']

    def send_invite_link(self, request, queryset):
        for q in queryset:
            q.send_invite_mail(request)

    send_invite_link.short_description = "Envoyer le lien d'invitation"

admin.site.register(UserInvite, UserInviteModelAdmin)

admin.site.unregister(Group)