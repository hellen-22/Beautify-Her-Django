from django.urls import path
from rest_framework_nested import routers

from . import views


urlpatterns = [
    path('customer/', views.CustomerRegistrationGenericApiView.as_view(), name='customer-register'),
    path('customer/<int:pk>/', views.CustomerProfileRetrieveUpdateDeleteGenericApiView.as_view(), name='cutomer-details'),

    path('service-provider/', views.ServiceProviderRegistrationGenericApiView.as_view(), name='service-provider-register'),
    path('service-provider/<int:pk>/', views.ServiceProviderProfileRetrieveUpdateDeleteGenericApiView.as_view(), name='service-provider-details'),
]