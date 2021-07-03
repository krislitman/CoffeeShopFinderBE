from rest_framework import serializers
from .models import CoffeeShop, FavoriteShop
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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
