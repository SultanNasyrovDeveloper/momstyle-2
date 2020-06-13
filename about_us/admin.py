from django.contrib import admin
from . import models


class AboutUsBlockImageAdmin(admin.TabularInline):
    model = models.AboutUsBlockImage
    extra = 1


@admin.register(models.AboutUsBlock)
class AboutUsBlockAdmin(admin.ModelAdmin):
    inlines = (AboutUsBlockImageAdmin, )



