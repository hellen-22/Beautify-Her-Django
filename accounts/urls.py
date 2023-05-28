from django.urls import path, include
from rest_framework_nested import routers

from . import views
from services.views import *

router =  routers.DefaultRouter()
router.register('register-customer', views.CustomerRegistrationViewSet, basename='register-customer')
router.register('register-service-provider', views.ServiceProviderRegistrationViewSet, basename='register-service-provider')
router.register('user', views.UserViewSet, basename='user')
router.register('customer', views.CustomerViewSet, basename='customer')
router.register('service-provider', views.ServiceProviderViewSet, basename='provider')


urlpatterns = router.urls