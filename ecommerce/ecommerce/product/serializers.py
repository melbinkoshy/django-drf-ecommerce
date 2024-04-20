from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    field="__all__"

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    field="__all__"

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    field="__all__"