# Generated by Django 2.2.6 on 2020-06-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='size',
            new_name='sizes',
        ),
    ]
