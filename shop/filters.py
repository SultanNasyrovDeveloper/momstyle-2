import django_filters as filters
from django import forms
from . import models


class ProductFilter(filters.FilterSet):

    price = filters.RangeFilter()
    available = filters.ChoiceFilter(
        choices=((None, 'Не указано'), (True, 'В наличии'), (False, 'Под заказ')),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = filters.ModelMultipleChoiceFilter(
        queryset=models.ProductCategory.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    sizes = filters.ModelMultipleChoiceFilter(
        queryset=models.ProductSize.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = models.Product
        fields = ('available', 'category', 'sizes', 'price')

