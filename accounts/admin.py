from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import UserInvite

User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    # form = UserChangeForm
    # add_form = UserCreationForm
    # change_password_form = AdminPasswordChangeForm
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "first_name", "last_name")
    ordering = ()
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
class UserInviteModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'email_sent', 'verified']
    actions = ['send_invite_link']

    def send_invite_link(self, request, queryset):
        for q in queryset:
            q.send_invite_mail(request)

    send_invite_link.short_description = "Envoyer le lien d'invitation"

admin.site.register(UserInvite, UserInviteModelAdmin)

admin.site.unregister(Group)