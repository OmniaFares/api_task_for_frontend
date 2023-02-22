from django.contrib import admin

from .models import SliderImage, Category, Brand, Item

admin.site.register(SliderImage)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Item)