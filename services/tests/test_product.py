import pytest
from decimal import Decimal
from model_bakery import baker
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from services.models import *
from accounts.models import *

@pytest.mark.django_db
class TestCreateProduct():
    def test_if_is_admin_return_201(self, authenticate_user, api_client):
        authenticate_user()

        category = baker.make(ProductCategory)

        product = {
            "name": "Hair Food",
            "category": category.id,
            "price": Decimal('8.09'),
            "slug": "-"
        }

        response = api_client.post('/services/product/', product, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_authenticated_and_is_provider_return_201(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user)

        category = baker.make(ProductCategory)
        # image_file = SimpleUploadedFile(
        #     "test_image.jpg",
        #     b"file_content_bytes",
        #     content_type="image/jpg"
        # )

        # print(image_file)

        product = {
            "name": "Hair Food",
            "category": category.id,
            "price": Decimal('3.99'),
        }

        response = api_client.post('/services/product/', product, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_authenticated_and_not_provider_return_403(self, api_client, authorize_user):
        user = baker.make(User, is_staff=False, role='is_customer')

        authorize_user(user=user) 

        category = baker.make(ProductCategory)

        product = {
            "name": "Hair Food",
            "category": category.id,
            "price": Decimal('8.09'),
            "slug": "-"
        }

        response = api_client.post('/services/product/', product, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_not_authenticated_return_401(self, api_client):
        category = baker.make(ProductCategory)

        product = {
            "name": "Hair Food",
            "category": category.id,
            "price": Decimal('8.09'),
            "slug": "-"
        }

        response = api_client.post('/services/product/', product, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_valid_return_201(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user) 

        category = baker.make(ProductCategory)

        product = {
            "name": "Hair Food",
            "category": category.id,
            "price": Decimal('8.09'),
            "slug": "-"
        }

        response = api_client.post('/services/product/', product, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user) 

        category = baker.make(ProductCategory)

        product = {
            "name": "",
            "category": category.id,
            "price": Decimal('8.09'),
            "slug": "-"
        }

        response = api_client.post('/services/product/', product, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestGetProduct():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/services/product/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, api_client):
        response = api_client.get('/services/product/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestRetrieveProduct():
    def test_if_is_authenticated_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        product = baker.make(Product)

        response = api_client.get(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_not_authenticated_return_401(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_product_exists_return_200(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        product = baker.make(Product)

        response = api_client.get(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_product_doesnt_exists_return_404(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        product = baker.make(Product)
        product.delete()

        response = api_client.get(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
class TestUpdateProduct():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        product = baker.make(Product)

        update_data = {
            "name": "Hair Food",
            "price": Decimal('8.09'),
        }

        response = api_client.patch(f'/services/product/{product.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK


    def test_if_is_authenticated_and_is_provider_return_200(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user)

        product = baker.make(Product)

        update_data = {
            "name": "Hair Food",
            "price": Decimal('8.09'),
        }

        response = api_client.patch(f'/services/product/{product.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_authenticated_and_not_provider_return_403(self, api_client, authorize_user):
        user = baker.make(User, is_staff=False, role='is_customer')

        authorize_user(user=user)

        product = baker.make(Product)

        update_data = {
            "name": "Hair Food",
            "price": Decimal('8.09'),
        }

        response = api_client.patch(f'/services/product/{product.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_200(self, api_client, authorize_user):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user)

        product = baker.make(Product)

        update_data = {
            "name": "Hair Food",
            "price": Decimal('8.09'),
        }

        response = api_client.patch(f'/services/product/{product.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_return_400(self, api_client, authorize_user):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user)

        product = baker.make(Product)

        update_data = {
            "name": "",
            "price": Decimal('8.09'),
        }

        response = api_client.patch(f'/services/product/{product.id}/', update_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestDeleteProduct():
    def test_if_is_admin_return_204(self, authenticate_user, api_client):
        authenticate_user()

        product = baker.make(Product)

        response = api_client.delete(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_authenticated_and_is_service_provider_return_204(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role='is_provider')

        authorize_user(user=user)

        product = baker.make(Product)

        response = api_client.delete(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_authenticated_and_not_service_provider_return_403(self, authorize_user, api_client):
        user = baker.make(User, is_staff=False, role='is_customer')

        authorize_user(user=user)

        product = baker.make(Product)

        response = api_client.delete(f'/services/product/{product.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


        