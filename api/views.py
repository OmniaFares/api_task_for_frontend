from .models import SliderImage, Category, Brand, Item
from .serializer import (
    SliderImageSerializer,
    CategorySerializer,
    BrandSerializer,
    ItemSerializer,
)
from rest_framework import viewsets, mixins


class SliderImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SliderImage.objects.all()
    serializer_class = SliderImageSerializer

    def get_queryset(self):
        if self.action == "list":
            return [self.queryset.order_by("?").first()]
        return super().get_queryset()


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ItemsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
