from django.contrib import admin

from . import models


@admin.register(models.PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass
