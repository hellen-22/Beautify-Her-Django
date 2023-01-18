from django.shortcuts import render
from rest_framework import viewsets, generics, permissions

from .serializers import *
from .models import *


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceListSerializer
        return ServiceSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    