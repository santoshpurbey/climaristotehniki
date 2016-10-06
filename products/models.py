from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image

from portfolio.models import Category

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    description = RichTextField()
    description_en = RichTextField()
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', default=1)
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = models.TextField()
    short_description_en = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    specifications = RichTextField()
    specifications_en = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
