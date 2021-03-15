```python
from videos.models import Video
from playlists.models import Playlist

video_a = Video.objects.create(title='My title', video_id='abc123')

print(video_a)

print(dir(video_a))

playlist_a = Playlist.objects.create(title='This is my title', video=video_a)

print(dir(playlist_a))

print(playlist_a.video_id)

print(video_a.id)
```

```python
playlist_a.video = None
playlist_a.save()
print(playlist_a.video_id)
print(video_a.playlist_set.all())
```

```python
playlist_a.video = video_a
playlist_a.save()
print(video_a.playlist_set.all())
print(playlist_a.id)
```


```python
print(video_a.playlist_set.all().published())

print(Playlist.objects.all().published())

print(Playlist.objects.filter(video=video_a).published())
```