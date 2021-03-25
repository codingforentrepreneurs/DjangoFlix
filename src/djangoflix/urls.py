"""djangoflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from playlists.views import (
    MovieListView, 
    MovieDetailView,
    PlaylistDetailView,
    SearchView,
    TVShowListView, 
    TVShowDetailView,
    TVShowSeasonDetailView,
    FeaturedPlaylistListView
)

from ratings.views import rate_object_view

'''
str - everything but /
int - 0 and up
slug -> this-is-a-slug-1
uuid - import uuid; uuid.uuid4()
path -> abc/bac/asdfads/

<int:myvar>
'''


urlpatterns = [
    path('', FeaturedPlaylistListView.as_view()),
    path('admin/', admin.site.urls),
    path('category/', include('categories.urls')),
    path('categories/', include('categories.urls')),
    path('movies/<slug:slug>/', MovieDetailView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('media/<int:pk>/', PlaylistDetailView.as_view()),
    path('search/', SearchView.as_view()),
    path('shows/<slug:showSlug>/seasons/<slug:seasonSlug>/', TVShowSeasonDetailView.as_view()),
    path('shows/<slug:slug>/seasons/', TVShowDetailView.as_view()),
    path('shows/<slug:slug>/', TVShowDetailView.as_view()),
    path('shows/', TVShowListView.as_view()),
    path('tags/', include('tags.urls')),
    path('object-rate/', rate_object_view)
]
