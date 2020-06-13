import django_filters as filters
from .models import Product


class ProductFilter(filters.FilterSet):

    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ('available', 'category', 'sizes', 'price')
