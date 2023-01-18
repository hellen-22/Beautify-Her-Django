from django.urls import path, include
from rest_framework_nested import routers

from . import views

router =  routers.DefaultRouter()
router.register('customer', views.CustomerRegistrationViewSet, basename='customer')
router.register('service-provider', views.ServiceProviderRegistrationViewSet, basename='service-provider')


urlpatterns = [
    path('', include(router.urls)),
]