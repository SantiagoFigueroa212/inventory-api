from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from .serializers import ProductSerializer, ReviewSerializer
from .models import Product, Review

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer