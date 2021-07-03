from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CoffeeShop, FavoriteShop
from django.contrib.auth.models import User
from .serializers import CoffeeShopSerializer, FavoriteShopSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoffeeShopViewSet(viewsets.ModelViewSet):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer

    @action(detail=True, methods=['POST'])
    def create_favorite(self, request, pk=None):
        # TODO add another endpoint to create favorite
        # TODO seperate from rating the shop
        if 'rating' in request.data:
            current_shop = CoffeeShop.objects.get(id=pk)
            current_user = request.user
            rating = request.data['rating']
            shop = FavoriteShop.objects.create(
                user=current_user,
                coffeeshop=current_shop,
                rating=rating
            )
            serialized = FavoriteShopSerializer(shop, many=False)
            response = {
                'message': 'Favorite Shop Added',
                'favorite': serialized.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'message': 'You must provide a rating'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class FavoriteShopViewSet(viewsets.ModelViewSet):
    queryset = FavoriteShop.objects.all()
    serializer_class = FavoriteShopSerializer
    authentication_classes = (TokenAuthentication, )

    @action(detail=True, methods=['POST'])
    def rate_shop(self, request, pk=None):
        if 'rating' in request.data:
            shop = FavoriteShop.objects.get(id=pk)
            shop.rating = request.data['rating']
            response = {
                'message': 'Rating updated'
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'message': 'You must provide a rating'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
