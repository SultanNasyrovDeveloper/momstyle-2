from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    sizes = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = models.Product
        fields = (
            'id', 'available', 'name', 'prev_price', 'price', 'material', 'models_height',
            'description', 'category', 'sizes', 'images',
        )

