from django.db import models


class BeerType(models.Model):  # Пиво: розливне|пляшкове
    name = models.CharField(max_length=50)  # "Тип пива"
    description = models.TextField()  # "Опис"

    def __str__(self):
        return self.name


class Brewery(models.Model):  # Броварні
    name = models.CharField(max_length=50)  # 'Назва броварні'
    description = models.TextField()  # 'Опис броварні'

    def __str__(self):
        return self.name


class BeerVolume(models.Model):
    name = models.CharField(default='0', max_length=50)

    def __str__(self):
        return self.name


class BeerStyle(models.Model):  # Стиль пива: IPA/Stout|etc.
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SnackType(models.Model):  # Тип закуски: холодна|гаряча
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Beer(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    beer_style = models.ForeignKey(BeerStyle, on_delete=models.CASCADE)  # 'Стиль'
    name = models.CharField(default=" ", max_length=30)
    description = models.TextField()
    abv = models.PositiveSmallIntegerField()  # 'ABV (Відсоток алкоголю)'
    og = models.PositiveSmallIntegerField()  # 'OG (Щільність)'
    ibu = models.PositiveSmallIntegerField()  # 'IBU (Гіркота)'
    volume = models.ManyToManyField(BeerVolume, through="Options")

    def __str__(self):
        return self.name


class Options(models.Model):  # Варіації пива та об'єму
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    volume = models.ForeignKey(BeerVolume, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()


