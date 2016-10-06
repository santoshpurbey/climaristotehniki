from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.


class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique_for_date='publish')
    body = RichTextField()
    body_en = RichTextField()
    publish = models.DateTimeField( auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image = models.ImageField(upload_to='page', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=120)
    subtitle_en = models.CharField(max_length=120)
    image = models.ImageField(upload_to='slider')

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


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



class Faq(models.Model):
    question = models.CharField(max_length=200)
    question_en = models.CharField(max_length=200)
    answer = RichTextField()
    answer_en = RichTextField()
    category = models.ForeignKey(Category, related_name='faqs', default=1)

    class Meta:
        ordering = ('question',)
        verbose_name = "faq"
        verbose_name_plural = "faqs"

    def __unicode__(self):
        return self.question
