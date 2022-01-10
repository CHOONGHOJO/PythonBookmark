from django.urls import path
from .views import BookmarkListView, BookmarkCreateView

urlpatterns = [
    #http://127.0.0.1/bookmark/
    #
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
]