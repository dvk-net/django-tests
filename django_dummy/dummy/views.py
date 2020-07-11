from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse

from .models import ForTesting

class DummyList(ListView):
    template_name = "dummy/list.html"
    model = ForTesting

class DummyListAuth(LoginRequiredMixin, ListView):
    template_name = "dummy/list.html"
    model = ForTesting


class DummyListAuth(LoginRequiredMixin, CreateView):
    template_name = "dummy/create.html"
    model = ForTesting
    success_url = 'dummy-list-auth/'
    fields = [
        'name',
        'description'
    ]

class DummyListAuth(LoginRequiredMixin, CreateView):
    template_name = "dummy/create.html"
    model = ForTesting
    success_url = 'dummy-list-auth/'
    fields = [
        'name',
        'description'
    ]

class DummyUpdateAuth(LoginRequiredMixin, UpdateView):
    template_name = "dummy/create.html"
    model = ForTesting
    success_url = 'dummy-list-auth/'
    fields = [
        'name',
        'description'
    ]
# Create your views here.
