from rest_framework import serializers

from shop.serializers import ProductSerializer


class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, instance):
        return instance.get_total_price()


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)
    items_number = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    def get_items_number(self, instance):
        return instance.get_total_price()

    def get_total_ptice(self, instance):
        return instance.get_total_price()

