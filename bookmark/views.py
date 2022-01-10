from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# class형, 함수형 view
# web page에 점속한다 -> page를 본다
# URL을 입력 -> web server가 view를 찾아서 동작시킨다 -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'