from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(title='This is my title', video_id='abc')
        self.obj_b = Video.objects.create(title='This is my title', state=Video.VideoStateOptions.PUBLISH, video_id='abasdfdsc')

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)
    
    def test_valid_title(self):
        title='This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 2)
    
    def test_draft_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(
            state=Video.VideoStateOptions.PUBLISH,
            publish_timestamp__lte= now 
        )
        self.assertTrue(published_qs.exists())
        