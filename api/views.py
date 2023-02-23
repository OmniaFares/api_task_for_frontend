from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .models import SliderImage, Category, Brand, Item
from .serializer import SliderImageSerializer, CategorySerializer, BrandSerializer, ItemSerializer


class SliderImagesViewSet(ViewSet):

    @action(detail=True, methods=['get'])
    def get_image(self, request):
        item = SliderImage.objects.order_by('?').first()
        serializer = SliderImageSerializer(item)
        return Response(serializer.data)
    

class CategoryViewSet(ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(ViewSet):
    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ItemsViewSet(ViewSet):
    queryset = Item.objects.all()

    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)