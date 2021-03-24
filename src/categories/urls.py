from django.urls import path

from .views import CategoryListView, CategoryDetailView


urlpatterns = [
    path('<slug:slug>/', CategoryDetailView.as_view()),
    path('', CategoryListView.as_view())
]