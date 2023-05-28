from django.shortcuts import render
from django.db.models import Sum
from rest_framework import viewsets, generics, permissions

from .serializers import *
from .models import *
from .permissions import *

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [permissions.IsAdminUser]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceListSerializer
        return ServiceSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser]
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ViewProductSerializer
        return ProductSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PATCH', 'DELETE', 'PUT']:
            return [IsServiceProviderOrAdmin()]
        return [permissions.IsAuthenticated()]
    

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer


    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
    

"""The view for service uploading"""
class ServiceUploadViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceUploadSerializer
    queryset = ServiceUpload.objects.all()

    def get_serializer_context(self):
        return {'user': self.request.user }

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsServiceProviderOrAdmin()]
        return [IsOwnerOrReadOnly(), permissions.IsAuthenticated()]

"""The view to enable customer booking appointment"""
class AppointmentBookingViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'customer_id': self.kwargs['customer_pk']}

    def get_queryset(self):
        return BookAppointment.objects.filter(customer_id=self.kwargs['customer_pk']).select_related('customer')

