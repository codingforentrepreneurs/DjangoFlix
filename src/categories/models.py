from django.contrib.contenttypes.fields import GenericRelation

from django.db import models

from tags.models import TaggedItem

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=220)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = GenericRelation(TaggedItem, related_query_name='category')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'