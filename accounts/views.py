from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated


from .serializers import *
from .models import *

#Registration views.
class CustomerRegistrationGenericApiView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegistrationSerializer

#Retrieve, Update and Delete Profiles views
class CustomerProfileRetrieveUpdateDeleteGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    #permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CustomerUpdateSerializer
        return CustomerRegistrationSerializer
        

#Registration view
#Need to remove the Listing of Profiles
class ServiceProviderRegistrationGenericApiView(generics.ListCreateAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderRegistrationSerializer

#Retrieve, Update and Delete Profiles views
class ServiceProviderProfileRetrieveUpdateDeleteGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceProvider.objects.all()
    #permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ServiceProviderUpdateSerializer
        return ServiceProviderRegistrationSerializer
