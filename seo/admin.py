from django.contrib import admin
from.models import SitePageSeo, ProductPageSeo


@admin.register(SitePageSeo)
class SitePageSeoAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductPageSeo)
class ProductPageSeoAdmin(admin.ModelAdmin):
    pass
