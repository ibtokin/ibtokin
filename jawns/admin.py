from django.contrib import admin


class ContentAdmin(admin.ModelAdmin):
    model = Content
    def get_context_data(self, **kwargs):
        context = super(ContentAdmin, self).get_context_data(**kwargs)
        return context

admin.site.register(Content, ContentAdmin)
