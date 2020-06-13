from rest_framework import serializers

from shop.serializers import ProductSerializer

from .cart import CartItem, Cart


class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    size = serializers.CharField(max_length=20)
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)

    def get_total_price(self, instance):
        return instance.get_total_price()

    def create(self, validated_data):
        return CartItem(
            product_id=validated_data.get('product_id'),
            quantity=validated_data.get('quantity'),
            size=validated_data.get('size'),
        )


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)
    items_number = serializers.SerializerMethodField(read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)

    def get_items_number(self, instance):
        return instance.get_total_price()

    def get_total_price(self, instance):
        return instance.get_total_price()

    def create(self, validated_data):
        items = []
        if 'items' in validated_data:
            items = [CartItem(**item) for item in validated_data['items']]
        return Cart(items=items)

