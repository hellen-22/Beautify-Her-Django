from decimal import Decimal
from django.db import transaction
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

class ViewProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'image', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cartItem:CartItem):
        return cartItem.quantity * cartItem.product.price

        
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


class AddCartItemSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item

        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'added_at', 'cart_items']


"""A serializer to enable uploading of services by service providers"""
class ServiceUploadSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['user']
        provider = ServiceProvider.objects.get(user=user)

        service_upload = ServiceUpload.objects.create(provider=provider, **validated_data)
        return service_upload

    class Meta:
        model = ServiceUpload
        fields = ['id', 'service', 'price', 'images', 'rating']

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id']

"""A Serializer to enable booking of appointment by customers"""
class AppointmentBookingSerializer(serializers.ModelSerializer):
    customer = CustomerDetailSerializer(read_only=True)
    
    def create(self, validated_data):
        user = self.context['user']
        customer = Customer.objects.get(user=user)

        book_appointment = BookAppointment.objects.create(customer=customer, **validated_data)
        return book_appointment

        
    class Meta:
        model = BookAppointment
        fields = ['id', 'service', 'provider', 'customer', 'date', 'time']


"""Order Item Details"""
class OrderItemsDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price_of_item = serializers.SerializerMethodField()

    def get_total_price_of_item(self, orderitem:OrderItem):
        return Decimal(orderitem.quantity) * orderitem.product.price

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total_price_of_item']
        
"""Order Serializer"""
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsDetailsSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, orderitems:OrderItem):
        return sum([item.quantity * item.product.price for item in orderitems.order_items.all()])

    class Meta:
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'order_items', 'total_price']
 
"""Create Order Serializer"""
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.CharField()

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']
            user = self.context['user']

            customer = Customer.objects.get(user=user)

            order = Order.objects.create(customer=customer)
            cart_items = CartItem.objects.select_related('product').filter(cart_id=cart_id)

            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )
                for item in cart_items
            ]

            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(pk=cart_id).delete()

            return order

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']