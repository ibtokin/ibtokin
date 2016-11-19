from django.contrib import admin
from jawns.models import Content, They


class TheyAdmin(admin.ModelAdmin):
    model = They
    def get_context_data(self, **kwargs):
        context = super(TheyAdmin, self).get_context_data(**kwargs)
        return context
admin.site.register(They, TheyAdmin)

class ContentAdmin(admin.ModelAdmin):
    model = Content
    def get_context_data(self, **kwargs):
        context = super(ContentAdmin, self).get_context_data(**kwargs)
        return context

admin.site.register(Content, ContentAdmin)
