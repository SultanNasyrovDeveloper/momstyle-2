from django.contrib import admin

from . import models


@admin.register(models.DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    pass
