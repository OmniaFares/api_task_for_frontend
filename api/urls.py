from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SliderImagesViewSet, CategoryViewSet, BrandViewSet, ItemsViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'items', ItemsViewSet)

urlpatterns = [
    path('slider_image', SliderImagesViewSet.as_view({'get': 'get_image'})),
    path('', include(router.urls)),
]