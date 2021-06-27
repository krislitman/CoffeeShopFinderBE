from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CoffeeShopViewSet, FavoriteShopViewSet

router = routers.DefaultRouter()
router.register('coffeeshops', CoffeeShopViewSet)
router.register('favoriteshops', FavoriteShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
