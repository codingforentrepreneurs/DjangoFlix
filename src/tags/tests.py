from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.db.utils import IntegrityError
# Create your tests here.

from playlists.models import Playlist

from .models import TaggedItem

class TaggedItemTestCase(TestCase):
    def setUp(self):
        ply_title = "New title"
        self.ply_obj = Playlist.objects.create(title=ply_title)
        self.ply_obj2 = Playlist.objects.create(title=ply_title)
        self.ply_title = ply_title
        self.ply_obj.tags.add(TaggedItem(tag='new-tag'), bulk=False)
        self.ply_obj2.tags.add(TaggedItem(tag='new-tag'), bulk=False)

    def test_content_type_is_not_null(self):
        with self.assertRaises(IntegrityError):
            TaggedItem.objects.create(tag='my-new-tag')

    def test_create_via_content_type(self):
        c_type = ContentType.objects.get(app_label='playlists', model='playlist')
        # c_type.model_class()
        tag_a = TaggedItem.objects.create(content_type=c_type, object_id=1, tag='new-tag')
        self.assertIsNotNone(tag_a.pk)
        tag_a = TaggedItem.objects.create(content_type=c_type, object_id=100, tag='new-tag2')
        self.assertIsNotNone(tag_a.pk)

    def test_create_via_model_content_type(self):
        c_type = ContentType.objects.get_for_model(Playlist)
        tag_a = TaggedItem.objects.create(content_type=c_type, object_id=1, tag='new-tag')
        self.assertIsNotNone(tag_a.pk)

    def test_create_via_app_loader_content_type(self):
        PlaylistKlass = apps.get_model(app_label='playlists', model_name='Playlist')
        c_type = ContentType.objects.get_for_model(PlaylistKlass)
        tag_a = TaggedItem.objects.create(content_type=c_type, object_id=1, tag='new-tag')
        self.assertIsNotNone(tag_a.pk)
    
    def test_related_field(self):
        self.assertEqual(self.ply_obj.tags.count(), 1)

    def test_related_field_create(self):
        self.ply_obj.tags.create(tag='another-new-tag')
        self.assertEqual(self.ply_obj.tags.count(), 2)

    def test_related_field_query_name(self):
        qs = TaggedItem.objects.filter(playlist__title__iexact=self.ply_title)
        self.assertEqual(qs.count(), 2)

    def test_related_field_via_content_type(self):
        c_type = ContentType.objects.get_for_model(Playlist)
        tag_qs = TaggedItem.objects.filter(content_type=c_type, object_id=self.ply_obj.id)
        self.assertEqual(tag_qs.count(), 1)

    def test_direct_obj_creation(self):
        obj = self.ply_obj
        tag = TaggedItem.objects.create(content_object=obj, tag='another1')
        self.assertIsNotNone(tag.pk)