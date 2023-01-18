from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated


from .serializers import *
from .models import *
from services.models import *

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


class ServiceUploadViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceUploadSerializer
    #permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'provider_id': self.kwargs['provider_pk']}

    def get_queryset(self):
        return ServiceUpload.objects.filter(provider_id=self.kwargs['provider_pk'])


class AppointmentBookingViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentBookingSerializer
    #permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'customer_id': self.kwargs['customer_pk']}

    def get_queryset(self):
        return BookAppointment.objects.filter(customer_id=self.kwargs['customer_pk'])