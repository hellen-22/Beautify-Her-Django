from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .serializers import *
from .models import *
from .permissions import *
from services.models import *

"""Creation of customers accounts"""
class CustomerRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegistrationSerializer
    http_method_names = ['post']

"""Customer details, updating and deleting"""    
class CustomerViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CustomerUpdateSerializer
        return CustomerRegistrationSerializer
    
    def get_queryset(self):
        if (self.request.user.is_staff):
            return Customer.objects.all().select_related('user')
        return Customer.objects.filter(user=self.request.user).select_related('user')
    
            

"""Creation of service provider account"""
class ServiceProviderRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderRegistrationSerializer
    http_method_names = ['post']


"""Service Provider details, updating and deleting""" 
class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all().select_related('user')
    http_method_names = ['get', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ServiceProviderUpdateSerializer
        return ServiceProviderRegistrationSerializer


"""A list of all users"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAdminUser]