from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image


class Project(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = models.CharField(max_length=200)
    short_description_en = models.CharField(max_length=200)
    description = RichTextField()
    description_en = RichTextField()
    start_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio')

    class Meta:
        ordering = ['-start_date', ]

    def __unicode__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


def get_image_path(instance, filename):
    return '/'.join(['project_images', instance.project.slug, filename])


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=1)
    image = models.ImageField(upload_to=get_image_path)

    # add this bit in after our model
    def save(self, *args, **kwargs):
        # this is required when you override save functions
        super(ProjectImage, self).save(*args, **kwargs)
        # our new code
        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (1240, 700)

            if i_width > 1240:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
            elif i_height > 700:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)


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
    name_en = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = models.TextField()
    short_description_en = models.TextField()
    description = RichTextField()
    description_en = RichTextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    specifications = RichTextField()
    specifications_en = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = RichTextField()
    question_en = RichTextField()
    answer = RichTextField()
    answer_en = RichTextField()
    category = models.ForeignKey(Category, related_name='faqs', default=1)


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
    image = models.ImageField(upload_to='page')
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
