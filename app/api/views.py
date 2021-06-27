from django.shortcuts import render
from rest_framework import viewsets
from .models import CoffeeShop, FavoriteShop
from .serializers import CoffeeShopSerializer, FavoriteShopSerializer


class CoffeeShopViewSet(viewsets.ModelViewSet):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer


class FavoriteShopViewSet(viewsets.ModelViewSet):
    queryset = FavoriteShop.objects.all()
    serializer_class = FavoriteShopSerializer
