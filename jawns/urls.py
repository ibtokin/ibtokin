from django.conf.urls import url
<<<<<<< HEAD
from .views import  ContentDetailView, ContentListView

=======
from jawns.views import  ContentDetailView, ContentListView
>>>>>>> cdb1cb6b20af189919aa977d8d5995e3bc087c9f

urlpatterns = [
    url(r'^$', ContentListView.as_view(), name='content-list'),
    url(r'^(?P<slug>[-\w]+)/$', ContentDetailView.as_view(), name='content_detail'),

]
