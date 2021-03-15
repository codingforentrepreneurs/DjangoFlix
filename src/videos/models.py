from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True) # 'this-is-my-video'
    video_id = models.CharField(max_length=220)
    active = models.BooleanField(default=True)
    # timestamp
    # updated 
    # state 
    # publish_timestamp
    
    @property
    def is_published(self):
        return self.active

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'