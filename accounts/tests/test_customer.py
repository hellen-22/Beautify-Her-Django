from collections import OrderedDict
from rest_framework import status
import pytest
from model_bakery import baker

from accounts.models import *

@pytest.mark.django_db
class TestCreateCustomer():
    def test_if_data_is_valid_return_201(self, api_client):
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }
        response = api_client.post('/register-customer/', customer, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, api_client):
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': '',
                'bio': '',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }

        response = api_client.post('/register-customer/', customer, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_method_not_allowed_return_405(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)
        
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }

        response = api_client.post('/customer/', customer, format='json')

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    
    
@pytest.mark.django_db
class TestGetCustomers():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/customer/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/customer/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, api_client):
        response = api_client.get('/customer/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        


@pytest.mark.django_db
class TestRetrieveCustomer():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user()

        customer = baker.make(Customer)

        response = api_client.get(f'/customer/{customer.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, api_client):
        customer = baker.make(Customer)

        response = api_client.get(f'/customer/{customer.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_customer_exists_return_200(self, authenticate_user, api_client):
        authenticate_user()

        customer = baker.make(Customer)

        user = customer.user

        response = api_client.get(f'/customer/{customer.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_customer_doesnt_exists_return_404(self, authenticate_user, api_client):
        authenticate_user()

        customer = baker.make(Customer)
        customer.delete()

        response = api_client.get(f'/customer/{customer.id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        
        
@pytest.mark.django_db
class TestUpdateCustomer():
    def test_if_data_is_valid_return_200(self, api_client, authenticate_user):
        authenticate_user()

        customer_ = baker.make(Customer)
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }
        response = api_client.put(f'/customer/{customer_.id}/', customer, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_return_400(self, api_client, authenticate_user):
        authenticate_user()

        customer_ = baker.make(Customer)
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': '',
                'bio': '',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }

        response = api_client.put(f'/customer/{customer_.id}/', customer, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user()

        customer_ = baker.make(Customer)
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }
        response = api_client.put(f'/customer/{customer_.id}/', customer, format='json')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_not_authenticated_return_401(self, api_client):
        customer_ = baker.make(Customer)
        customer = {
            'user': {
                'username': 'Test',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'bio': 'Testing me',
                'password': 'Password',
                'confirm_password': 'Password'
            }
        }
        response = api_client.put(f'/customer/{customer_.id}/', customer, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestDeleteCustomer():
    def test_if_is_authenticated_return_204(self, authenticate_user, api_client):
        authenticate_user()

        customer = baker.make(Customer)

        response = api_client.delete(f'/customer/{customer.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_not_authenticated_return_401(self, authenticate_user, api_client):
        customer = baker.make(Customer)

        response = api_client.delete(f'/customer/{customer.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED