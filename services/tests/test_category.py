import pytest
from rest_framework import status

from model_bakery import baker
from services.models import *


@pytest.mark.django_db
class TestCreateCategory():
    def test_if_is_admin_return_201(self, authenticate_user, api_client):
        authenticate_user()

        service_category = {
            "category_name": "Dreadlocks",
        }

        product_category = {
            "name": "Hair food"
        }

        response = api_client.post('/services/service-category/', service_category, format='json')
        response2 = api_client.post('/services/product-category/', product_category, format='json')

        assert ((response.status_code == status.HTTP_201_CREATED) and (response2.status_code == status.HTTP_201_CREATED))


    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_category = {
            "category_name": "Dreadlocks",
        }

        product_category = {
            "name": "Hair food"
        }

        response = api_client.post('/services/service-category/', service_category, format='json')
        response2 = api_client.post('/services/product-category/', product_category, format='json')

        assert ((response.status_code == status.HTTP_403_FORBIDDEN) and (response2.status_code == status.HTTP_403_FORBIDDEN))

    def test_if_data_is_valid_return_201(self, authenticate_user, api_client):
        authenticate_user()

        service_category = {
            "category_name": "Dreadlocks",
        }

        product_category = {
            "name": "Hair food"
        }

        response = api_client.post('/services/service-category/', service_category, format='json')
        response2 = api_client.post('/services/product-category/', product_category, format='json')

        assert ((response.status_code == status.HTTP_201_CREATED) and (response2.status_code == status.HTTP_201_CREATED))


    def test_if_data_is_invalid_return_400(self, authenticate_user, api_client):
        authenticate_user()

        service_category = {
            "category_name": "Dreadlocks",
        }

        product_category = {
            "name": "Hair food"
        }

        response = api_client.post('/services/service-category/', product_category, format='json')
        response2 = api_client.post('/services/product-category/', service_category, format='json')

        assert ((response.status_code == status.HTTP_400_BAD_REQUEST) and (response2.status_code == status.HTTP_400_BAD_REQUEST))

@pytest.mark.django_db
class TestGetCategories():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/services/service-category/')
        response2 = api_client.get('/services/product-category/')

        assert ((response.status_code == status.HTTP_200_OK) and (response2.status_code == status.HTTP_200_OK))

    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/services/service-category/')
        response2 = api_client.get('/services/product-category/')

        assert ((response.status_code == status.HTTP_403_FORBIDDEN) and (response2.status_code == status.HTTP_403_FORBIDDEN))

@pytest.mark.django_db
class TestRetrieveCategories():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        product_category = baker.make(ProductCategory)

        response = api_client.get(f'/services/service-category/{service_category.id}/')
        response2 = api_client.get(f'/services/product-category/{product_category.id}/')

        assert ((response.status_code == status.HTTP_200_OK) and (response2.status_code == status.HTTP_200_OK))

    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_category = baker.make(ServiceCategory)
        product_category = baker.make(ProductCategory)

        response = api_client.get(f'/services/service-category/{service_category.id}/')
        response2 = api_client.get(f'/services/product-category/{product_category.id}/')

        assert ((response.status_code == status.HTTP_403_FORBIDDEN) and (response2.status_code == status.HTTP_403_FORBIDDEN))


    def test_if_category_exists_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        product_category = baker.make(ProductCategory)

        response = api_client.get(f'/services/service-category/{service_category.id}/')
        response2 = api_client.get(f'/services/product-category/{product_category.id}/')

        assert ((response.status_code == status.HTTP_200_OK) and (response2.status_code == status.HTTP_200_OK))

    
    def test_if_category_doesnt_exists_return_404(self, authenticate_user, api_client):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        product_category = baker.make(ProductCategory)

        service_category.delete()
        product_category.delete()

        response = api_client.get(f'/services/service-category/{service_category.id}/')
        response2 = api_client.get(f'/services/product-category/{product_category.id}/')

        assert ((response.status_code == status.HTTP_404_NOT_FOUND) and (response2.status_code == status.HTTP_404_NOT_FOUND))

@pytest.mark.django_db
class TestUpdateCategory():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        service_update_data = {
            "category_name": "Dreadlocks",
        }

        product_category = baker.make(ProductCategory)
        product_update_data = {
            "name": "Hair food"
        }

        response = api_client.put(f'/services/service-category/{service_category.id}/', service_update_data, format='json')
        response2 = api_client.put(f'/services/product-category/{product_category.id}/', product_update_data, format='json')

        assert ((response.status_code == status.HTTP_200_OK) and (response2.status_code == status.HTTP_200_OK))


    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        service_category = baker.make(ServiceCategory)
        service_update_data = {
            "category_name": "Dreadlocks",
        }

        product_category = baker.make(ProductCategory)
        product_update_data = {
            "name": "Hair food"
        }

        response = api_client.put(f'/services/service-category/{service_category.id}/', service_update_data, format='json')
        response2 = api_client.put(f'/services/product-category/{product_category.id}/', product_update_data, format='json')

        assert ((response.status_code == status.HTTP_403_FORBIDDEN) and (response2.status_code == status.HTTP_403_FORBIDDEN))

    def test_if_data_is_valid_return_200(self, authenticate_user, api_client):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        service_update_data = {
            "category_name": "Dreadlocks",
        }

        product_category = baker.make(ProductCategory)
        product_update_data = {
            "name": "Hair food"
        }

        response = api_client.put(f'/services/service-category/{service_category.id}/', service_update_data, format='json')
        response2 = api_client.put(f'/services/product-category/{product_category.id}/', product_update_data, format='json')


        assert ((response.status_code == status.HTTP_200_OK) and (response2.status_code == status.HTTP_200_OK))


    def test_if_data_is_invalid_return_400(self, authenticate_user, api_client):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        service_update_data = {
            "category_name": "Dreadlocks",
        }

        product_category = baker.make(ProductCategory)
        product_update_data = {
            "name": "Hair food"
        }

        response = api_client.put(f'/services/service-category/{service_category.id}/', product_update_data, format='json')
        response2 = api_client.put(f'/services/product-category/{product_category.id}/', service_update_data, format='json')

        assert ((response.status_code == status.HTTP_400_BAD_REQUEST) and (response2.status_code == status.HTTP_400_BAD_REQUEST))

@pytest.mark.django_db
class TestDeleteCategory():
    def test_if_is_admin_return_204(self, api_client, authenticate_user):
        authenticate_user()

        service_category = baker.make(ServiceCategory)
        product_category = baker.make(ProductCategory)

        response = api_client.delete(f'/services/service-category/{service_category.id}/')
        response2 = api_client.delete(f'/services/product-category/{product_category.id}/')

        assert ((response.status_code == status.HTTP_204_NO_CONTENT) and (response2.status_code == status.HTTP_204_NO_CONTENT))


    def test_if_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        service_category = baker.make(ServiceCategory)
        product_category = baker.make(ProductCategory)

        response = api_client.delete(f'/services/service-category/{service_category.id}/')
        response2 = api_client.delete(f'/services/product-category/{product_category.id}/')

        assert ((response.status_code == status.HTTP_403_FORBIDDEN) and (response2.status_code == status.HTTP_403_FORBIDDEN))

