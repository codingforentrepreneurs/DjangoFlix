from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from djangoflix.db.models import PublishStateOptions

from videos.models import Video
from .models import Playlist

class PlaylistModelTestCase(TestCase):
    def setUp(self):
        video_a = Video.objects.create(title='My title', video_id='abc123')
        self.video_a = video_a
        self.obj_a = Playlist.objects.create(title='This is my title', video=video_a)
        self.obj_b = Playlist.objects.create(title='This is my title', state=PublishStateOptions.PUBLISH, video=video_a)

    def test_playlist_video(self):
        self.assertEqual(self.obj_a.video, self.video_a)

    def test_video_playlist(self):
        qs = self.video_a.playlist_set.all()
        self.assertEqual(qs.count(), 2)

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)
    
    def test_valid_title(self):
        title='This is my title'
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(), 2)
    
    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Playlist.objects.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte= now 
        )
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published()
        published_qs_2 = Playlist.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs_2.count())
        