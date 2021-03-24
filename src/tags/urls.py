from django.urls import path

from .views import TaggedItemListView, TaggedItemDetailView

urlpatterns = [
    path("<slug:tag>", TaggedItemDetailView.as_view()),
    path('', TaggedItemListView.as_view()),
]