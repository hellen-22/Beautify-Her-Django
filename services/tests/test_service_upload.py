import pytest
from decimal import Decimal
from model_bakery import baker
from rest_framework import status
from django.core.files.uploadedfile import TemporaryUploadedFile

from services.models import *
from accounts.models import *


# @pytest.mark.django_db
# class TestCreateServiceUpload():
    

@pytest.mark.django_db
class TestGetServiceUpload():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/service-upload/')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_is_not_authenticated_return_401(self, api_client):
        response = api_client.get('/service-upload/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
class TestRetrieveServiceUpload():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_upload = baker.make(ServiceUpload)

        response = api_client.get(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_200_OK


    def test_if_is_not_authenticated_return_401(self, authenticate_user, api_client):
        service_upload = baker.make(ServiceUpload)

        response = api_client.get(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    
    def test_if_upload_exists_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_upload = baker.make(ServiceUpload)

        response = api_client.get(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_upload_doesnt_exists_return_404(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_upload = baker.make(ServiceUpload)
        service_upload.delete()

        response = api_client.get(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
class TestUpdateServiceUpload():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service_upload = baker.make(ServiceUpload)

        update_data = {
            "price": Decimal('2.20')
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK
    
    def test_if_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_upload = baker.make(ServiceUpload)

        update_data = {
            "price": Decimal('2.20')
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_is_authenticated_and_is_service_provider_and_is_owner_return_200(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_provider")

        authorize_user(user=user)
        provider = baker.make(ServiceProvider, user=user)
        service_upload = baker.make(ServiceUpload, provider=provider)

        update_data = {
            "price": Decimal('2.20')
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_authenticated_and_is_service_provider_and_not_owner_return_403(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_provider")

        authorize_user(user=user)
        another_user = baker.make(User, is_staff=False, role="is_provider")
        provider = baker.make(ServiceProvider, user=another_user)

        service_upload = baker.make(ServiceUpload, provider=provider)

        update_data = {
            "price": Decimal('2.20')
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_is_authenticated_and_is_not_service_provider_return_403(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_customer")

        authorize_user(user=user)
        service_upload = baker.make(ServiceUpload)

        update_data = {
            "price": Decimal('2.20')
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_200(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_provider")

        authorize_user(user=user)
        provider = baker.make(ServiceProvider, user=user)
        service_upload = baker.make(ServiceUpload, provider=provider)

        update_data = {
            "price": Decimal('2.20')
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_return_400(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_provider")

        authorize_user(user=user)
        provider = baker.make(ServiceProvider, user=user)
        service_upload = baker.make(ServiceUpload, provider=provider)

        update_data = {
            "price": ''
        }

        response = api_client.patch(f'/service-upload/{service_upload.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestDeleteServiceUpload():
    def test_if_is_admin_return_204(self, authenticate_user, api_client):
        authenticate_user()

        service_upload = baker.make(ServiceUpload)

        response = api_client.delete(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_upload = baker.make(ServiceUpload)

        response = api_client.delete(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_is_authenticated_and_is_service_provider_and_is_owner_return_204(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_provider")

        authorize_user(user=user)
        provider = baker.make(ServiceProvider, user=user)
        service_upload = baker.make(ServiceUpload, provider=provider)


        response = api_client.delete(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_authenticated_and_is_service_provider_and_not_owner_return_403(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_provider")

        authorize_user(user=user)
        another_user = baker.make(User, is_staff=False, role="is_provider")
        provider = baker.make(ServiceProvider, user=another_user)

        service_upload = baker.make(ServiceUpload, provider=provider)

        response = api_client.delete(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_is_authenticated_and_is_not_service_provider_return_403(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role="is_customer")

        authorize_user(user=user)
        service_upload = baker.make(ServiceUpload)

        response = api_client.patch(f'/service-upload/{service_upload.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN
