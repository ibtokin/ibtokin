from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^jawns/', include('jawns.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('jawns.urls')),
]
