from django.db import models
from django.utils.text import slugify


class SportType(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SportType, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=250)
    type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    photo = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    e_mail = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name