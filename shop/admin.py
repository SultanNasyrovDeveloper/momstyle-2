from django.contrib import admin
from .models import (ProductSize, ProductCategory, Product, ProductImage,
                     Order, OrderItem, ContactPerson)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductImageTabular(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'material', 'display']
    list_editable = ['display']
    list_filter = ['category', 'price', 'display']
    search_fields = ['name', 'material']
    inlines = [ProductImageTabular]


class OrderItemTabular(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['name', 'size', 'price', 'quantity', 'subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabular]
    list_display = ['customer', 'phone_number', 'date', 'processed']
    list_filter = ['processed', 'date']
    search_fields = ['name']


@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'processed']






