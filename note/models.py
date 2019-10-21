from django.db import models
import datetime
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)


    slug = models.SlugField(default='' , null = True , blank= True)
    active = models.BooleanField(default=True)
    tags = models.CharField(blank=True, max_length=100)

    img = models.ImageField(upload_to="notes_img")

    def save(self, *args , **kwargs):
        if not self.slug and self.title :
            self.slug = slugify(self.title)
        super(Note , self).save(*args , **kwargs)

    def split_tag(self):
        return self.tags.split(',')


    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Note'
        ordering = ['-created']

    def __str__(self):
        return self.title
