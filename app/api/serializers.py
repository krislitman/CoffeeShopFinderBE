from rest_framework import serializers
from .models import CoffeeShop, FavoriteShop


class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeShop
        fields = (
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
        )


class FavoriteShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteShop
        fields = (
            'id',
            'coffeeshop',
            'user',
            'rating'
        )
