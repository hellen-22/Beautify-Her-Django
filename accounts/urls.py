from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('register-customer', views.CustomerRegistrationViewset, basename='register')
router.register('register-service-provider', views.ServiceProviderRegistrationViewset, basename='register1')

urlpatterns = router.urls