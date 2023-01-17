from django.db import transaction
from rest_framework import serializers

from .models import *

class UserDetailsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=50, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, max_length=50, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'password', 'confirm_password']


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']

            if password == confirm_password:
                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], bio=user['bio'], password=password)

                customer = CustomerProfile.objects.create(user=user)

                return customer
            
            else:
                raise serializers.ValidationError('Passwords do not match')

    class Meta:
        model = CustomerProfile
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

                service_provider = ServiceProviderProfile.objects.create(user=user, location=self.validated_data['location'], phone_number=self.validated_data['phone_number'])

                return service_provider
            
            else:
                raise serializers.ValidationError('Passwords do not match')


    class Meta:
        model = ServiceProviderProfile
        fields = ['user', 'location', 'phone_number']