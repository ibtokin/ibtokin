from django.views.generic.detail import DetailView, ListView
from django.shortcuts import render
from django.http import HttpResponse
from models import They, Content
import datetime

def index(request):
    return HttpResponse("Coming Soon: Content!")

def detail(request, jawn_id):
    return HttpResponse("Content # %s" % content_id)

class ContentDetailView(DetailView):
    model = Content

    def get_context_data(self, **kwargs):
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ContentListView(ListView):
    model = Content

    def get_context_data(self, **kwargs):
        context = super(ContentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
