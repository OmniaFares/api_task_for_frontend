from rest_framework import serializers

from .models import SliderImage, Category, Brand, Item


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ['image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['sale_percentage', 'image']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'image', 'price_before_sale', 'price_after_sale']