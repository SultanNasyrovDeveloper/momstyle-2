from django.contrib import admin
from .models import (ProductSize, ProductCategory, Product, ProductImage)
from seo.models import ProductPageSeo


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductSeoTabularInline(admin.StackedInline):
    model = ProductPageSeo


class ProductImageTabular(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'material', 'display']
    list_editable = ['display']
    list_filter = ['category', 'price', 'display']
    search_fields = ['name', 'material']
    inlines = [ProductImageTabular, ProductSeoTabularInline]






