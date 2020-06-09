from django.contrib import admin
from .models import Banner, SiteMain, DeliveryPaymentInfo


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteMain)
class SiteMainAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Базовые', {'fields': ('logo', )}),
        ('Текст', {'fields': (('category_h2', 'category_par'), ('product_h2', 'product_par'))}),
        ('Ссылки', {'fields': ('insta_url', 'vk_url')}),
        ('Контакты', {'fields': ('phone_number', 'email', 'address', 'working_hours')}),
        ('Остальное', {'fields': ('delivery_header_image', 'about_header_image')}),

    )


@admin.register(DeliveryPaymentInfo)
class DeliveryPaymentInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
