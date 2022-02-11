from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Açıqlama')
    image = models.ImageField(null=True, blank=False)
    publishing_date = models.DateTimeField(verbose_name='Çəkilmə tarixi')
    choices = (
        ('drawing', "Rəsm"),
        ('design', "Dizayn")
    )
    drawing_or_design = models.CharField(max_length=10, choices=choices, verbose_name='Rəsm və ya Dizayn', blank=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'id': self.id})
    def get_delete_url(self):
        return reverse('gallery:delete', kwargs={'id': self.id})