from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
from djangoflix.db.models import PublishStateOptions
from djangoflix.db.receivers import publish_state_pre_save, slugify_pre_save

from videos.models import Video


class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte= now 
        )

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

class Playlist(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video = models.ForeignKey(Video, related_name='playlist_featured', blank=True, null=True, on_delete=models.SET_NULL) # one video per playlist
    videos = models.ManyToManyField(Video, related_name='playlist_item', blank=True, through='PlaylistItem')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = PlaylistManager()
    
    @property
    def is_published(self):
        return self.active
    

pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)

class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-timestamp']