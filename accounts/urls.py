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

customer_router = routers.NestedDefaultRouter(router, 'customer', lookup='customer')
customer_router.register('appointment', AppointmentBookingViewSet, basename='appointment')

service_provider_router = routers.NestedDefaultRouter(router, 'service-provider', lookup='provider')
service_provider_router.register('service-upload', ServiceUploadViewSet, basename='service-upload')

urlpatterns = router.urls + customer_router.urls + service_provider_router.urls