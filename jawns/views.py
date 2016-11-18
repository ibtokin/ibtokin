from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from jawns.models import They, Content



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
