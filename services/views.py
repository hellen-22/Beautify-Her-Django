from django.shortcuts import render
from django.db.models import Sum
from rest_framework import viewsets, generics, permissions

from .serializers import *
from .models import *
from accounts.models import User
from .permissions import *

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [permissions.IsAdminUser]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().select_related('category')
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceListSerializer
        return ServiceSerializer
    
    
"""The view for service uploading"""
class ServiceUploadViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceUploadSerializer
    queryset = ServiceUpload.objects.all()

    def get_serializer_context(self):
        return {'user': self.request.user }

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsServiceProviderOrAdmin()]
        return [IsServiceOwnerOrReadOnly(), permissions.IsAuthenticated()]
    

"""The view to enable customer booking appointment"""
class AppointmentBookingViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentBookingSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
    
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsCustomerOrAdmin()]
        return [IsAppointmentOwnerOrReadOnly(), permissions.IsAuthenticated()]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            User.objects.select_related()
            return BookAppointment.objects.all().select_related('customer')

        elif self.request.user.role == 'is_customer':
            return BookAppointment.objects.filter(customer__user=self.request.user).select_related('customer')
        
        elif self.request.user.role == 'is_provider':
            return BookAppointment.objects.filter(provider__user=self.request.user).select_related('customer')
        


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser]
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category')

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
    queryset = CartItem.objects.all().select_related('product')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateCartItemSerializer
        return CartItemSerializer


    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
    


"""Orders view"""
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_context(self):
        return {'user': self.request.user}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateOrderSerializer
        return OrderSerializer
    
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemsSerializer
    http_method_names = ['get']
