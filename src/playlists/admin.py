from django.contrib import admin

from tags.admin import TaggedItemInline

from .models import MovieProxy, TVShowProxy, TVShowSeasonProxy, Playlist, PlaylistItem, PlaylistRelated


class MovieProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ['title']
    fields = ['title', 'description', 'state', 'category', 'video', 'slug']
    class Meta:
        model = MovieProxy

    def get_queryset(self, request):
        return MovieProxy.objects.all()

admin.site.register(MovieProxy, MovieProxyAdmin)


class SeasonEpisodeInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0

class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline, SeasonEpisodeInline]
    list_display = ['title', 'parent']
    class Meta:
        model = TVShowSeasonProxy
    
    def get_queryset(self, request):
        return TVShowSeasonProxy.objects.all()

admin.site.register(TVShowSeasonProxy, TVShowSeasonProxyAdmin)


class TVShowSeasonProxyInline(admin.TabularInline):
    model = TVShowSeasonProxy
    extra = 0
    fields = ['order', 'title', 'state']

class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline, TVShowSeasonProxyInline]
    list_display = ['title']
    fields = ['title', 'description', 'state', 'category', 'video', 'slug']
    class Meta:
        model = TVShowProxy
    
    def get_queryset(self, request):
        return TVShowProxy.objects.all()

admin.site.register(TVShowProxy, TVShowProxyAdmin)


class PlaylistRelatedInline(admin.TabularInline):
    model = PlaylistRelated
    fk_name = 'playlist'
    extra = 0

class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistRelatedInline, PlaylistItemInline, TaggedItemInline]
    fields = [
        'title',
        'description',
        'slug',
        'state',
        'active'
    ]
    class Meta:
        model = Playlist

    
    def get_queryset(self, request):
        return Playlist.objects.filter(type=Playlist.PlaylistTypeChoices.PLAYLIST)

admin.site.register(Playlist, PlaylistAdmin)