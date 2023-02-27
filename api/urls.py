from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import SliderImagesViewSet, CategoryViewSet, BrandViewSet, ItemsViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("brands", BrandViewSet)
router.register("items", ItemsViewSet)
router.register("slider_image", SliderImagesViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("", include(router.urls)),
    path(
        "docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
