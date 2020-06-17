from django.contrib import admin

from . import models


class OrderItemAdminInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0
    readonly_fields = ('total_price', )


class OrderPersonalInfoInline(admin.StackedInline):
    model = models.OrderPersonalInformation


class OrderPaymentInformationInline(admin.TabularInline):
    model = models.OrderPaymentInformation


class OrderDeliveryInformationInline(admin.StackedInline):
    model = models.OrderDeliveryInformation


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price', )
    inlines = (
        OrderPaymentInformationInline,
        OrderDeliveryInformationInline,
        OrderPaymentInformationInline,
        OrderItemAdminInline,
    )
