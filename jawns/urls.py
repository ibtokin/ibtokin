from django.conf.urls import url
from .views import  ContentDetailView, ContentListView


urlpatterns = [
    url(r'^$', ContentListView.as_view(), name='content-list'),
    url(r'^(?P<slug>[-\w]+)/$', ContentDetailView.as_view(), name='content_detail'),

]
