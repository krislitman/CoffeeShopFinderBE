from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class CoffeeShop(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    location = models.JSONField(blank=False)
    is_closed = models.BooleanField(default=True)
    categories = models.JSONField(blank=True)
    url = models.CharField(max_length=1000, blank=True)
    image_url = models.CharField(max_length=1000, blank=True)
    rating = models.IntegerField(blank=True)
    phone = models.CharField(max_length=1000, blank=True)
    yelp_id = models.CharField(max_length=1000, unique=True, blank=False)


class FavoriteShop(models.Model):
    coffeeshop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, validators=[MinValueValidator(1),
                                                         MaxValueValidator(10)])
