import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'momstyle_2.settings')
import django
django.setup()
from shop.models import Product, ProductCategory, ProductSize
import random



SIZES = ['XS', 'S', 'M', 'L', '46', '48', '50']

def populate_category():

    category_names = []

    for i in range(4):
        category_name = 'Категория {}'.format(i)
        ProductCategory.objects.create(name=category_name)
        print('Создание категории "{}"'.format(category_name))
        category_names.append(category_name)

    return category_names


def populate_sizes():
    for item in SIZES:
        ProductSize.objects.create(name=item)
        print('Создание размера - {}'.format(item))


def populate_products(categories, sizes):

    price = 1500
    material = 'Хлопок 100%'
    models_height = 165
    description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                  'Etiam sodales justo non ipsum viverra vulputate. ' \
                  'Mauris commodo sit amet sapien eu congue. ' \
                  'Donec efficitur nunc vitae sem condimentum, non maximus tellus dictum. ' \
                  'Sed turpis ipsum, consectetur eget augue quis, fermentum pulvinar lectus.'

    for i in range(15):
        item_name = 'Название товара {}'.format(i)
        category = ProductCategory.objects.get(name=random.choice(categories))
        product_sizes = random.sample(sizes, random.choice([2, 3, 4]))

        product = Product(name=item_name, category=category, price=price, material=material,
                          models_height=models_height, description=description)
        product.save()
        for i in product_sizes:
            size = ProductSize.objects.get(name=i)
            product.size.add(size)
        print('Создание товара {}'.format(item_name))


if __name__ == '__main__':
    print('Заполнение базы данных магазина момстайл')
    categories = populate_category()
    populate_sizes()
    populate_products(categories, SIZES)

    print('Заполнение базы данных окончено')