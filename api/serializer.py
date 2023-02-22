from rest_framework import serializers

from .models import SliderImage, Category, Brand, Item


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'