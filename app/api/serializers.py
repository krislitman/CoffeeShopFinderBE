from rest_framework import serializers
from .models import CoffeeShop, FavoriteShop


class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        type = CoffeeShop
        attributes = {
            'id',
            'name',
            'location',
            'is_closed',
            'categories',
            'url',
            'image_url',
            'rating',
            'phone',
            'yelp_id'
        }


class FavoriteShopSerializer(serializers.ModelSerializer):
    class Meta:
        type = FavoriteShop
        attributes = {
            'id',
            'coffeeshop',
            'user',
            'rating'
        }
