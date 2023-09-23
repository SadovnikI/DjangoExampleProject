from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.product_views import ProductViewSet
from products.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='CustomUser')
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    path('', include(router.urls)),
]
