from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated


from .serializers import *
from .models import *

#Registration views.
class CustomerRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CustomerUpdateSerializer
        return CustomerRegistrationSerializer
            

#Registration view
#Need to remove the Listing of Profiles
class ServiceProviderRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ServiceProviderUpdateSerializer
        return ServiceProviderRegistrationSerializer

