import hashlib

from django.conf import settings


def get_payment_url(order_id, total_price):
    template = (
        'https://auth.robokassa.ru/Merchant/Index.aspx?MerchantLogin=MomstyleRu&'
        'InvId={order_id}&Culture=ru&Encoding=utf-8&OutSum={total_price},00&'
        'SignatureValue={signature}'
    )
    hash_base = f'{settings.PAYMENT_SHOP_NAME}:{total_price},00:{order_id}:{settings.PAYMENT_PASSWORD1}'

    url = template.format(
        shop_name=settings.PAYMENT_SHOP_NAME,
        order_id=order_id,
        total_price=total_price,
        signature=hashlib.md5(hash_base.encode('utf-8')).hexdigest(),
    )

    return url


