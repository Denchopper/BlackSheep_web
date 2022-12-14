from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class BeerType(models.Model):  # Пиво: розливне|пляшкове
    name = models.CharField(max_length=50, null=True)  # "Тип пива"
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BeerType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brewery(models.Model):  # Броварні
    name = models.CharField(max_length=50, null=True)  # 'Назва броварні'
    description = models.TextField()  # 'Опис броварні'
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brewery, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BeerVolume(models.Model):
    name = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return str(self.name)


class BeerStyle(models.Model):  # Стиль пива: IPA/Stout|etc.
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('style', kwargs={'beer_style_id': self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BeerStyle, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Beer(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.SET_NULL, null=True)
    beer_style = models.ForeignKey(BeerStyle, on_delete=models.SET_NULL, null=True)  # 'Стиль'
    beer_type = models.ForeignKey(BeerType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(default="", max_length=30, blank=True)
    description = models.TextField(blank=True)
    abv = models.DecimalField(max_digits=3, decimal_places=1)  # 'ABV (Відсоток алкоголю)'
    og = models.PositiveSmallIntegerField()  # 'OG (Щільність)'
    ibu = models.PositiveSmallIntegerField()  # 'IBU (Гіркота)'
    volume = models.ManyToManyField(BeerVolume)
    price_per_05 = models.PositiveSmallIntegerField(default='0')
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.beer_style)
        super(Beer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



