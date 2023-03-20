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
        provider_id = self.context['provider_id']
        provider = ServiceProvider.objects.get(id=provider_id)

        service_upload = ServiceUpload.objects.create(provider=provider, **validated_data)
        return service_upload

    class Meta:
        model = ServiceUpload
        fields = ['id', 'service', 'price', 'images', 'rating']


"""A Serializer to enable booking of appointment by customers"""
class AppointmentBookingSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        customer_id = self.context['customer_id']
        customer = Customer.objects.get(id=customer_id)

        book_appointment = BookAppointment.objects.create(customer=customer, **validated_data)
        return book_appointment

        
    class Meta:
        model = BookAppointment
        fields = ['id', 'service', 'provider', 'date', 'time']

 