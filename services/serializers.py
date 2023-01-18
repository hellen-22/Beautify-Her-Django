from rest_framework import serializers

from .models import *

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'category_name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'category']

class ServiceListSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer()

    class Meta:
        model = Service
        fields = ['id', 'name', 'category']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'image', 'price']