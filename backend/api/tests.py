from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product, Review


class ProductAPITest(APITestCase):

    def test_create_product(self):
        data = {
            "name": "Keyboard",
            "description": "Mechanical keyboard",
            "price": 1500,
            "stock": 10
        }

        response = self.client.post("/api/products/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Keyboard")

    def test_get_products(self):
        Product.objects.create(
            name="Mouse",
            description="Gaming mouse",
            price=800,
            stock=20
        )

        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product_with_invalid_price(self):
        data = {
            "name": "Keyboard",
            "description": "Mechanical keyboard",
            "price": -100,
            "stock": 10
        }

        response = self.client.post("/api/products/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReviewAPITest(APITestCase):

    def test_create_review(self):
        product = Product.objects.create(
            name="Keyboard",
            description="Mechanical keyboard",
            price=1500,
            stock=10
        )

        data = {
            "review": "Excellent keyboard!",
            "product": product.id
        }

        response = self.client.post("/api/reviews/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)

    def test_create_empty_review(self):
        product = Product.objects.create(
            name="Keyboard",
            description="Mechanical keyboard",
            price=1500,
            stock=10
        )

        data = {
            "review": "",
            "product": product.id
        }

        response = self.client.post("/api/reviews/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)