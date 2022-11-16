from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class SnackType(models.Model):  # Тип закуски: холодна|гаряча
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SnackType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(SnackType, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    price_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.name
