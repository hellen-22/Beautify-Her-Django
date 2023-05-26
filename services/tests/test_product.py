import pytest
from decimal import Decimal
from model_bakery import baker
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from services.models import *

@pytest.mark.django_db
class TestCreateProduct():
    def test_if_is_authenticated_return_201(self, authenticate_user, api_client):
        authenticate_user()

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



