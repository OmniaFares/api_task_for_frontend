from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .models import SliderImage, Category, Brand, Item
from .serializer import SliderImageSerializer, CategorySerializer, BrandSerializer, ItemSerializer


class SliderImagesViewSet(ViewSet):
    queryset = SliderImage.objects.order_by('?').first()
    serializer = SliderImageSerializer

    @action(detail=True, methods=['get'])
    def get_image(self, request):
        serializer = self.serializer(self.queryset)
        return Response(serializer.data)
    

class CategoryViewSet(ViewSet):
    queryset = Category.objects.all()
    serializer = CategorySerializer

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(ViewSet):
    queryset = Brand.objects.all()
    serializer = BrandSerializer

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data)


class ItemsViewSet(ViewSet):
    queryset = Item.objects.all()
    serializer = ItemSerializer

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data)