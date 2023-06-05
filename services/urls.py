from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('service-category', views.ServiceCategoryViewSet, basename='service-category')
router.register('service', views.ServiceViewSet, basename='service')
router.register('service-upload', views.ServiceUploadViewSet, basename='service-upload')
router.register('appointment', views.AppointmentBookingViewSet, basename='appointment')
router.register('product-category', views.ProductCategoryViewSet, basename='product-category')
router.register('product', views.ProductViewSet, basename='product')
router.register('cart', views.CartViewSet, basename='cart')
router.register('order', views.OrderViewSet, basename='order')

cart_routers = routers.NestedDefaultRouter(router, 'cart', lookup='cart')
cart_routers.register('cart-items', views.CartItemViewSet, basename='cart-items')


order_routers = routers.NestedDefaultRouter(router, 'order', lookup='order')
order_routers.register('order-items', views.OrderItemViewSet, basename='order-items')

urlpatterns = router.urls + cart_routers.urls + order_routers.urls
