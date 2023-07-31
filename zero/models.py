from django.db import models
from django.urls import reverse


class Man(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    content=models.TextField(blank=True, verbose_name='text')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    cat=models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})

    class Meta():
        verbose_name='famous men'
        verbose_name_plural='famous men'
        ordering=['time_create', 'title']

class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

    class Meta():
        verbose_name='Category'
        verbose_name_plural='Category'
        ordering=['id']