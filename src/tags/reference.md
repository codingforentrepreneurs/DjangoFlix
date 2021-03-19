## Ways to import a model
- [Docs](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/)

### Standard
```python
from playlists.models import Playlist
```


### Via Content Type
```python
from django.contrib.contenttypes.models import ContentType
playlist_type = ContentType.objects.get(app_label='playlists', model='playlist')
Playlist = playlist_type.model_class()
```

### Via Apps
```python
from django.apps import apps
Playlist = apps.get_model(app_label='playlists', model_name='Playlist')
```


## Ways to associate a generic foreign key

### With an model instance/object
```python
ply_obj = Playlist.objects.first()
TaggedItem.objects.create(content_object=ply_obj, tag='test-1')
```

### With an model content type and object id
```python
content_type = ContentType.objects.get_for_model(Playlist)
TaggedItem.objects.create(content_type=content_type, object_id=1, tag='test-2')
```


### Using GenericRelationField
#### 
```python
ply_obj.tags.add(TaggedItem(tag='New tag'), bulk=False)
```
or
```python
ply_obj.tags.create(tag='New tag too')
```