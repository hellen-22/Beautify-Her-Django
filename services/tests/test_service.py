import pytest
from model_bakery import baker
from rest_framework import status

from services.models import *


@pytest.mark.django_db
class TestCreateService():
    def test_if_is_admin_return_201(self, api_client, authenticate_user):
        authenticate_user()
        category = baker.make(ServiceCategory)

        service = {
            'name': 'ftgte',
            'category': category.id
        }

        response = api_client.post('/service/', service, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    
    def test_if_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        category = baker.make(ServiceCategory)
        service = {
            'name': 'Aclyric nails',
            'category': category.id
        }

        response = api_client.post('/service/', service)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_201(self, api_client, authenticate_user):
        authenticate_user()

        category = baker.make(ServiceCategory)
        service = {
            'name': 'Aclyric nails',
            'category': category.id
        }

        response = api_client.post('/service/', service, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, api_client, authenticate_user):
        authenticate_user()

        category = baker.make(ServiceCategory)
        service = {
            'name': '',
            'category': category.id
        }

        response = api_client.post('/service/', service, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestGetService():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/service/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/service/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
class TestRetrieveService():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)

        response = api_client.get(f'/service/{service.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service = baker.make(Service)

        response = api_client.get(f'/service/{service.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_service_exists_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)

        response = api_client.get(f'/service/{service.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_service_doesnt_exists_return_404(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)
        service.delete()

        response = api_client.get(f'/service/{service.id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        
@pytest.mark.django_db
class TestUpdateService():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)
        update_data = {
            "name": "Change service"
        }

        response = api_client.patch(f'/service/{service.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service = baker.make(Service)
        update_data = {
            "name": "Change service"
        }

        response = api_client.patch(f'/service/{service.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)
        update_data = {
            "name": "Change service"
        }

        response = api_client.patch(f'/service/{service.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_invalid_return_400(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)
        update_data = {
            "name": ""
        }

        response = api_client.patch(f'/service/{service.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestDeleteService():
    def test_if_is_admin_return_204(self, authenticate_user, api_client):
        authenticate_user()

        service = baker.make(Service)

        response = api_client.delete(f'/service/{service.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service = baker.make(Service)

        response = api_client.delete(f'/service/{service.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN