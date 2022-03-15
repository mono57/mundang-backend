from django.contrib import admin

from quotes.models import Quote, QuoteTag



class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ('author',)

admin.site.register(Quote, QuoteModelAdmin)

class QuoteTagModelAdmin(admin.ModelAdmin):
    list_display = QuoteTag.admin_list_display()
    populated_fields = QuoteTag.admin_populated_fields()

admin.site.register(QuoteTag, QuoteTagModelAdmin)
