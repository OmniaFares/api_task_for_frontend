from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to='api/images/sliders/')

    def __str__(self):
        return self.id


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='api/images/categories/')

    def __str__(self):
        return self.name


class Brand(models.Model):
    sale_percentage = models.FloatField()
    image = models.ImageField(upload_to='api/images/brands/')

    def __str__(self):
        return self.id


class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='api/images/items/')
    price_before_sale = models.FloatField()
    price_after_sale = models.FloatField()

    def __str__(self):
        return self.name