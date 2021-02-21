from django.shortcuts import render
from rest_framework import status, generics
from .models import Product, Category, Size
from .serializers import ProductSerializer, CategorySerializer, SizeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"
    max_page_size = 1000


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailsCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListSize(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class DetailsSize(generics.RetrieveUpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoryId", "sizeId"]
    pagination_class = StandardResultsSetPagination


class DetailsProduct(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
