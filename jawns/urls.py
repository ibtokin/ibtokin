from django.conf.urls import url
from jawns.views import  ContentDetailView, ContentListView

urlpatterns = [
    url(r'^$', ContentListView.as_view(), name='content-list'),
    url(r'^(?P<id>[-\w]+)/$', ContentDetailView.as_view(), name='content-detail'),
]
