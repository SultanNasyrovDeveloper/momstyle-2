from django.contrib import admin
from .models import Banner, SiteMain, DeliveryPaymentInfo, SocialLink


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteMain)
class SiteMainAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Базовые', {'fields': ('logo', 'sizes_table')}),
        ('Организация', {'fields': ('organisation_line1', 'organisation_line2', 'organisation_line3', 'organisation_line4')}),
        ('Текст', {'fields': (('category_h2', 'category_par'), ('product_h2', 'product_par'))}),
        ('Контакты', {'fields': ('phone_number', 'email', 'address', 'working_hours')}),
        ('Остальное', {'fields': ('delivery_header_image', 'about_header_image')}),
    )


@admin.register(DeliveryPaymentInfo)
class DeliveryPaymentInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

