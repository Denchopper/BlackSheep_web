from django.db import models


class BeerType(models.Model):  # Пиво: розливне|пляшкове
    name = models.CharField(max_length=50)  # "Тип пива"
    description = models.TextField()  # "Опис"


class Brewery(models.Model):  # Броварні
    name = models.CharField(max_length=50)  # 'Назва броварні'
    description = models.TextField()  # 'Опис броварні'


class BeerStyle(models.Model):  # Стиль пива: IPA/Stout|etc.
    name = models.CharField(max_length=50)


class SnackType(models.Model):  # Тип закуски: холодна|гаряча
    name = models.CharField(max_length=50)
    description = models.TextField()


class Beer(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    beer_style = models.ForeignKey(BeerStyle, on_delete=models.CASCADE)  # 'Стиль'
    description = models.TextField()
    abv = models.PositiveSmallIntegerField()  # 'ABV (Відсоток алкоголю)'
    og = models.PositiveSmallIntegerField()  # 'OG (Щільність)'
    ibu = models.PositiveSmallIntegerField()  # 'IBU (Гіркота)'
    price = models.PositiveSmallIntegerField()  # 'Ціна за 1 літр'



