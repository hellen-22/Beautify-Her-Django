from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated


from .serializers import *
from .models import *
from services.models import *

"""Creation of customers accounts"""
class CustomerRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegistrationSerializer
    http_method_names = ['post']

"""Customer details, updating and deleting"""    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().select_related('user')
    http_method_names = ['get', 'put', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CustomerUpdateSerializer
        return CustomerRegistrationSerializer
            

"""Creation of service provider account"""
class ServiceProviderRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderRegistrationSerializer
    http_method_names = ['post']


"""Service Provider details, updating and deleting""" 
class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all().select_related('user')

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ServiceProviderUpdateSerializer
        return ServiceProviderRegistrationSerializer


"""A list of all users"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    http_method_names = ['get']