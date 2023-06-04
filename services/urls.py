from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('service-category', views.ServiceCategoryViewSet, basename='service-category')
router.register('service', views.ServiceViewSet, basename='service')
router.register('service-upload', views.ServiceUploadViewSet, basename='service-upload')
router.register('book-appointment', views.AppointmentBookingViewSet, basename='book-appointment')
router.register('product-category', views.ProductCategoryViewSet, basename='product-category')
router.register('product', views.ProductViewSet, basename='product')
router.register('cart', views.CartViewSet, basename='cart')
router.register('order', views.OrderViewSet, basename='order')

cart_routers = routers.NestedDefaultRouter(router, 'cart', lookup='cart')
cart_routers.register('cart_items', views.CartItemViewSet, basename='cart_items')

urlpatterns = router.urls + cart_routers.urls
