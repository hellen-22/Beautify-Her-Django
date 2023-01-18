from django.db import transaction
from rest_framework import serializers

from .models import *
from services.models import *

class UserDetailsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=50, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, max_length=50, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'bio', 'password', 'confirm_password']


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']

            if password == confirm_password:
                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], bio=user['bio'], password=password)

                customer = Customer.objects.create(user=user)

                return customer
            
            else:
                raise serializers.ValidationError('Passwords do not match')

    class Meta:
        model = Customer
        fields = ['id', 'user']

class UserUpdateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'bio']

class CustomerUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateDetailsSerializer()

    def update(self, instance, validated_data):
        user_validated_data = validated_data.pop('user', None)

        user = instance.user

        user.first_name = user_validated_data.get('first_name', user.first_name)
        user.last_name = user_validated_data.get('last_name', user.last_name)
        user.username = user_validated_data.get('username', user.username)
        user.bio = user_validated_data.get('bio', user.bio)
        user.save()
        instance.save()

        return instance

    class Meta:
        model = Customer
        fields = ['user']


class ServiceProviderRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']

            if password == confirm_password:
                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], bio=user['bio'], password=password)

                service_provider = ServiceProvider.objects.create(user=user, location=self.validated_data['location'], phone_number=self.validated_data['phone_number'])

                return service_provider
            
            else:
                raise serializers.ValidationError('Passwords do not match')


    class Meta:
        model = ServiceProvider
        fields = ['id', 'user', 'location', 'phone_number']

class ServiceProviderUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateDetailsSerializer()


    def update(self, instance, validated_data):
        user_validated_data = validated_data.pop('user', None)

        user = instance.user

        user.first_name = user_validated_data.get('first_name', user.first_name)
        user.last_name = user_validated_data.get('last_name', user.last_name)
        user.username = user_validated_data.get('username', user.username)
        user.bio = user_validated_data.get('bio', user.bio)
        user.save()

        instance.location = validated_data.get('location', instance.location)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        return instance

    
    class Meta:
        model = ServiceProvider
        fields = ['user', 'location', 'phone_number']


class ServiceUploadSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        provider_id = self.context['provider_id']
        provider = ServiceProvider.objects.get(id=provider_id)

        service_upload = ServiceUpload.objects.create(provider=provider, **validated_data)
        return service_upload

    class Meta:
        model = ServiceUpload
        fields = ['id', 'service', 'price', 'images', 'rating']

class AppointmentBookingSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        customer_id = self.context['customer_id']
        customer = Customer.objects.get(id=customer_id)

        book_appointment = BookAppointment.objects.create(customer=customer, **validated_data)
        return book_appointment

        
    class Meta:
        model = BookAppointment
        fields = ['id', 'service', 'provider', 'date', 'time']