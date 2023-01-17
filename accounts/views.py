from django.shortcuts import render
from rest_framework import viewsets, mixins


from .serializers import *
from .models import *
# Create your views here.

class CustomerRegistrationViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerRegistrationSerializer

class ServiceProviderRegistrationViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ServiceProviderProfile.objects.all()
    serializer_class = ServiceProviderRegistrationSerializer