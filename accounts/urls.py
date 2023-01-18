from django.urls import path, include
from rest_framework_nested import routers

from . import views

router =  routers.DefaultRouter()
router.register('customer', views.CustomerRegistrationViewSet, basename='customer')
router.register('service-provider', views.ServiceProviderRegistrationViewSet, basename='provider')

customer_router = routers.NestedDefaultRouter(router, 'customer', lookup='customer')
customer_router.register('appointment', views.AppointmentBookingViewSet, basename='appointment')

service_provider_router = routers.NestedDefaultRouter(router, 'service-provider', lookup='provider')
service_provider_router.register('service-upload', views.ServiceUploadViewSet, basename='service-upload')

urlpatterns = router.urls + customer_router.urls + service_provider_router.urls