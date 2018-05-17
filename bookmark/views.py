from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark

class BookmarkCV(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    # template_name = "asdasd.html"
    # reverse url pattern -> url
    # lazy: without lazy->바로 url이 만들어져있는 형태
    # with lazy: 실행 할때 url을 만들어서 던져줌.
    success_url = reverse_lazy('bookmark:index')
    def form_valid(self, form):
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response({'form': form})

class BookmarkUV(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDV(LoginRequiredMixin, DetailView):
    model = Bookmark

class BookmarkRV(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')