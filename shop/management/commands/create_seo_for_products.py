from django.core.management.base import BaseCommand, CommandError
from shop.models import Product
from seo.models import ProductPageSeo


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for product in Product.objects.all():
            if not hasattr(product, 'page_seo'):
                ProductPageSeo.objects.create(product=product)
        self.stdout.write(self.style.SUCCESS('Successfully created seo pages'))
