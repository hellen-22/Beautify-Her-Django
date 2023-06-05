import pytest
from model_bakery import baker
from rest_framework import status

from accounts.models import *
from services.models import *


@pytest.mark.django_db
class TestCreateAppointment():
    def test_if_data_is_valid_return_201(self, authorize_user, api_client):
        user = baker.make(User, role="is_customer", is_staff=False)

        authorize_user(user=user)

        customer = baker.make(Customer, user=user)
        service = baker.make(Service)
        provider = baker.make(ServiceProvider)

        appointment = {
            'customer': customer.id,
            'service': service.id,
            'provider': provider.id,
            'date': '2023-01-22',
            'time': '13:00:00'
        }

        response = api_client.post(f'/appointment/', appointment)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, authorize_user, api_client):
        user = baker.make(User, role="is_customer", is_staff=False)

        authorize_user(user=user)

        customer = baker.make(Customer, user=user)
        service = baker.make(Service)
        provider = baker.make(ServiceProvider)

        appointment = {
            'customer': customer.id,
            'service': service.id,
            'provider': provider.id,
            'date': '',
            'time': ''
        }

        response = api_client.post(f'/appointment/', appointment)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_is_authenticated_and_is_customer_return_201(self, authorize_user, api_client):
        user = baker.make(User, role="is_customer", is_staff=False)

        authorize_user(user=user)

        customer = baker.make(Customer, user=user)
        service = baker.make(Service)
        provider = baker.make(ServiceProvider)

        appointment = {
            'customer': customer.id,
            'service': service.id,
            'provider': provider.id,
            'date': '2023-01-22',
            'time': '13:00:00'
        }

        response = api_client.post(f'/appointment/', appointment)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_authenticated_and_is_not_customer_return_403(self, authorize_user, api_client):
        user = baker.make(User, role="is_provider", is_staff=False)

        authorize_user(user=user)

        customer = baker.make(Customer)
        service = baker.make(Service)
        provider = baker.make(ServiceProvider)

        appointment = {
            'customer': customer.id,
            'service': service.id,
            'provider': provider.id,
            'date': '2023-01-22',
            'time': '13:00:00'
        }

        response = api_client.post(f'/appointment/', appointment)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_not_authenticated_return_401(self, authenticate_user, api_client):
        customer = baker.make(Customer)
        service = baker.make(Service)
        provider = baker.make(ServiceProvider)

        appointment = {
            'customer': customer.id,
            'service': service.id,
            'provider': provider.id,
            'date': '2023-01-22',
            'time': '13:00:00'
        }

        response = api_client.post(f'/appointment/', appointment)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    
@pytest.mark.django_db
class TestGetAppointment():
    def test_if_not_authenticated_return_401(self, api_client):
        response = api_client.get(f'/appointment/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestRetrieveAppointment():
    def test_if_not_authenticated_return_401(self, api_client):
        response = api_client.get(f'/appointment/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    
@pytest.mark.django_db
class TestDeleteAppointment():
    def test_if_not_authenticated_return_401(self, api_client):
        response = api_client.get(f'/appointment/')

        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED