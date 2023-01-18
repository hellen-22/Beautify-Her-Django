from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('service-category', views.ServiceCategoryViewSet, basename='service-category')
router.register('service', views.ServiceViewSet, basename='service')
router.register('product-category', views.ProductCategoryViewSet, basename='product-category')
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]
