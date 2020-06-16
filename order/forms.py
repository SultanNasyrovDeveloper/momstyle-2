from django import forms

from delivery.models import DeliveryMethod
from payment.models import PaymentMethod

from . import models


class OrderPersonalInformationForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    phone_number = forms.CharField(label='Номер телефона')
    email = forms.EmailField(label='Алрес электронной почты')

    first_name.widget.attrs.update({'class': 'form-control'})
    second_name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    phone_number.widget.attrs.update({'class': 'form-control', 'type': 'tel'})

    def clean_first_name(self):
        return self.cleaned_data['first_name'].title()

    def clean_second_name(self):
        return self.cleaned_data['second_name'].title()


class OrderDeliveryForm(forms.Form):
    delivery_method = forms.ModelChoiceField(
        queryset=DeliveryMethod.objects.all(), label='Способ доставки',
    )

    index = forms.CharField(label='Индекс')
    city = forms.CharField(label='Город')
    street = forms.CharField(label='Улица')
    building_number = forms.CharField(label='Номер дома')
    apartment = forms.CharField(label='Квартира', required=False)

    delivery_method.widget.attrs.update({'class': 'form-control'})
    index.widget.attrs.update({'class': 'form-control'})
    city.widget.attrs.update({'class': 'form-control'})
    street.widget.attrs.update({'class': 'form-control'})
    building_number.widget.attrs.update({'class': 'form-control'})
    apartment.widget.attrs.update({'class': 'form-control'})

    def clean_delivery_method(self):
        return self.cleaned_data['delivery_method'].id


class OrderPaymentMethodForm(forms.Form):
    payment_method = forms.ModelChoiceField(
        queryset=PaymentMethod.objects.all(), label='Способ оплаты',
    )
    payment_method.widget.attrs.update({'class': 'form-control'})

    def clean_payment_method(self):
        return self.cleaned_data['payment_method'].id


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ('created', )

    def clean(self):
        data = super().clean()
        if not any([
            data.get('no_connect', None),
            data.get('connect_by_phone', None),
            data.get('connect_by_whatsapp', None)
        ]):
            raise forms.ValidationError('Выберите один из предложенных вариантов.')
        return data


class QuickBuyForm(forms.Form):

    first_name = forms.CharField(max_length=250, label="Имя")
    phone_number = forms.CharField(max_length=50, label="Номер телефона")

    first_name.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Введите имя'}
    )
    phone_number.widget.attrs.update(
        {'class': 'form-control', 'type': 'tel', 'placeholder': 'Введите номер телефона'}
    )

    def save(self):
        order = models.Order.objects.create(fast_buy=True)
        personal = order.personal_info
        personal.first_name = self.cleaned_data['first_name']
        personal.phone_number = self.cleaned_data['phone_number']
        personal.save()
        return order
