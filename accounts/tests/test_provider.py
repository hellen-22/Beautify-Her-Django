from rest_framework import status
from rest_framework.test import APITestCase
import pytest
from model_bakery import baker

from accounts.models import *

@pytest.mark.django_db
class TestCreateServiceProvider():
    def test_if_data_is_valid_return_200(self, api_client):
        provider = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'gggghgh'
        }
        response = api_client.post('/register-service-provider/', provider, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, api_client):
        provider = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': '',
                'bio': '',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'gggghgh'
        }

        response = api_client.post('/register-service-provider/', provider, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    
    def test_method_not_allowed_return_405(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        provider = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'gggghgh'
        }
        response = api_client.post('/service-provider/', provider, format='json')

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
class TestGetServiceProviders():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/service-provider/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, api_client):
        response = api_client.get('/service-provider/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestRetrieveServiceProvider():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        provider = baker.make(ServiceProvider)

        response = api_client.get(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, api_client):
        provider = baker.make(ServiceProvider)

        response = api_client.get(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_provider_exists_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        provider = baker.make(ServiceProvider)


        response = api_client.get(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_provider_doesnt_exist_return_404(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        provider = baker.make(ServiceProvider)
        provider.delete()

        response = api_client.get(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        
        
@pytest.mark.django_db
class TestUpdateServiceProvider():
    def test_if_data_is_valid_return_200(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False)
        
        authorize_user(user=user)
        
        provider = baker.make(ServiceProvider, user=user)

    
        update_data = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'Testing'
        }
        response = api_client.put(f'/service-provider/{provider.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_return_400(self, api_client, authorize_user):
        user = baker.make(User, is_staff=False)

        authorize_user(user=user)

        provider = baker.make(ServiceProvider, user=user)
        update_data = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': '',
                'bio': '',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': '',
            'phone_number': ''
        }

        response = api_client.put(f'/service-provider/{provider.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_is_authenticated_return_200(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False)
        
        authorize_user(user=user)
        
        provider = baker.make(ServiceProvider, user=user)

    
        update_data = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'Testing'
        }
        response = api_client.put(f'/service-provider/{provider.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_not_authenticated_return_401(self, api_client):
        provider = baker.make(ServiceProvider)

        update_data = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'Testing'
        }

        response = api_client.put(f'/service-provider/{provider.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_not_authorized_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        provider = baker.make(ServiceProvider)

        update_data = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            },
            'location': 'Testing',
            'phone_number': 'Testing'
        }

        response = api_client.put(f'/service-provider/{provider.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
class TestDeleteServiceProvider():
    def test_if_is_authenticated_return_204(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False)

        authorize_user(user=user)

        provider = baker.make(ServiceProvider, user=user)

        response = api_client.delete(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_not_authenticated_return_401(self, api_client):
        provider = baker.make(ServiceProvider)

        response = api_client.delete(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_not_authorized_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        provider = baker.make(ServiceProvider)

        response = api_client.delete(f'/service-provider/{provider.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN
