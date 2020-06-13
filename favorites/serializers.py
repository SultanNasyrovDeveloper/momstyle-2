from rest_framework import serializers

from shop.serializers import ProductSerializer

from .favorites import FavoritesItem, Favorites


class FavoritesItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product = ProductSerializer(read_only=True)


class FavoritesSerializer(serializers.Serializer):

    items = FavoritesItemSerializer(many=True)

    def create(self, validated_data):
        items = []
        if 'items' in validated_data:
            items = [
                FavoritesItem(product_id=item.get('product_id'))
                for item in validated_data.get('items')
            ]
        return Favorites(items=items)