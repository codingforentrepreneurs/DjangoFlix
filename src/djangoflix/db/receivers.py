from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

from .models import PublishStateOptions
from .utils import get_unique_slug

def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishStateOptions.PUBLISH 
    is_draft = instance.state == PublishStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif is_draft:
        instance.publish_timestamp = None

def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)

def unique_slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = get_unique_slug(instance, size=5)