import pytest
from model_bakery import baker
from rest_framework import status

from accounts.models import *
from services.models import *


@pytest.mark.django_db
class TestCreateAppointment():
    def test_if_data_is_valid_return_201(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

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

        response = api_client.post(f'/customer/{customer.id}/appointment/', appointment)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        customer = baker.make(Customer)
        service = baker.make(Service)
        provider = baker.make(ServiceProvider)

        appointment = {
            'customer': customer.id,
            'service': service.id,
            'provider': provider.id,
            'date': '',
            'time': ''
        }

        response = api_client.post(f'/customer/{customer.id}/appointment/', appointment)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_is_authenticated_return_201(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

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

        response = api_client.post(f'/customer/{customer.id}/appointment/', appointment)

        assert response.status_code == status.HTTP_201_CREATED

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

        response = api_client.post(f'/customer/{customer.id}/appointment/', appointment)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    
@pytest.mark.django_db
class TestGetAppointment():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        appointment = baker.make(BookAppointment)

        response = api_client.get(f'/customer/{appointment.customer.id}/appointment/')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_not_authenticated_return_401(self, authenticate_user, api_client):
        appointment = baker.make(BookAppointment)

        response = api_client.get(f'/customer/{appointment.customer.id}/appointment/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestRetrieveAppointment():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        appointment = baker.make(BookAppointment)

        response = api_client.get(f'/customer/{appointment.customer.id}/appointment/{appointment.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, authenticate_user, api_client):
        appointment = baker.make(BookAppointment)

        response = api_client.get(f'/customer/{appointment.customer.id}/appointment/{appointment.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_appointment_exists_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        appointment = baker.make(BookAppointment)

        response = api_client.get(f'/customer/{appointment.customer.id}/appointment/{appointment.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': appointment.id,
            'customer': appointment.customer.id,
            'provider': appointment.provider.id,
            'service': appointment.service.id,
            'date': appointment.date,
            'time': appointment.time
        }


@pytest.mark.django_db
class TestDeleteAppointment():
    def test_if_is_authenticated_return_204(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        appointment = baker.make(BookAppointment)

        response = api_client.delete(f'/customer/{appointment.customer.id}/appointment/{appointment.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    
    def test_if_not_authenticated_return_401(self, authenticate_user, api_client):
        appointment = baker.make(BookAppointment)

        response = api_client.delete(f'/customer/{appointment.customer.id}/appointment/{appointment.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED