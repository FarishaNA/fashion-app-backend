from django.shortcuts import render

# Create your views here.
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# 1. API View for returning all stored categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 2. API View for returning 5 randomized categories to the home page banner
class HomeCategoryListView(APIView):
    def get(self, request):
        categories = list(Category.objects.all())
        # Randomize/shuffle the list items on every request
        random.shuffle(categories)
        sliced_categories = categories[:5]
        serializer = CategorySerializer(sliced_categories, many=True)
        return Response(serializer.data, status=status.HTTP_OK)

# 3. Search endpoint matching user query keys with product titles
class SearchProductView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query:
            # title__icontains performs case-insensitive partial matching
            products = Product.objects.filter(title__icontains=query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_OK)
        return Response({"message": "No search query provided"}, status=status.HTTP_BAD_REQUEST)import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# 1. API View for returning all stored categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 2. API View for returning 5 randomized categories to the home page banner
class HomeCategoryListView(APIView):
    def get(self, request):
        categories = list(Category.objects.all())
        # Randomize/shuffle the list items on every request
        random.shuffle(categories)
        sliced_categories = categories[:5]
        serializer = CategorySerializer(sliced_categories, many=True)
        return Response(serializer.data, status=status.HTTP_OK)

# 3. Search endpoint matching user query keys with product titles
class SearchProductView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query:
            # title__icontains performs case-insensitive partial matching
            products = Product.objects.filter(title__icontains=query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_OK)
        return Response({"message": "No search query provided"}, status=status.HTTP_BAD_REQUEST)