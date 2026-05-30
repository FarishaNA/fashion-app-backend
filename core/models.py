from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imageUrl = models.URLField(blank=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    clothesType = models.CharField(max_length=50, default="unisex") # men, women, kids, unisex
    ratings = models.FloatField(default=1.0)
    colors = models.JSONField(default=list)
    sizes = models.JSONField(default=list)
    imageUrls = models.JSONField(default=list)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title