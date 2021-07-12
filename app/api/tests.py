from django.test import TestCase
import unittest
import pdb
import json
from rest_framework.test import APIRequestFactory, APIClient, RequestsClient
from .models import CoffeeShop, FavoriteShop


class CoffeeShopTest(unittest.TestCase):
    def setUp(self):
        CoffeeShop.objects.create(
            name='Starbucks',
            is_closed=True,
            location={"Tampa": "FL"},
            yelp_id='fakeid123'
        )
        CoffeeShop.objects.create(
            name='Kahwa Coffee',
            is_closed=False,
            location={"Tampa": "FL"},
            yelp_id='fakeid321'
        )
        ging = CoffeeShop.objects.create(
            name='Gingerbeard Coffee',
            is_closed=True,
            location={"Tampa": "FL"},
            yelp_id='fakeid987'
        )
        client = RequestsClient()
        self.response = client.get('http://localhost:8000/api/v1/coffeeshops/')
        self.response_two = client.get(
            'http://localhost:8000/api/v1/coffeeshops/{}'.format(ging.id))

    def tearDown(self):
        CoffeeShop.objects.all().delete()

    def test_coffee_shop_can_be_retrieved(self):
        shops = json.loads(self.response.content)
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(shops[0]['name'], 'Starbucks')
        self.assertEqual(shops[1]['name'], 'Kahwa Coffee')
        self.assertEqual(shops[2]['name'], 'Gingerbeard Coffee')
        self.assertEqual(CoffeeShop.objects.count(), 3)

    def test_can_return_a_single_coffee_shop(self):
        shop = json.loads(self.response_two.content)
        self.assertEqual(self.response_two.status_code, 200)
        self.assertEqual(shop['name'], 'Gingerbeard Coffee')


if __name__ == '__main__':
    unittest.main()
