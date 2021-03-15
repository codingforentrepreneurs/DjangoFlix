from django.contrib import admin

# Register your models here.
from .models import Video, VideoProxy

admin.site.register(Video)


admin.site.register(VideoProxy)