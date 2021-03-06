# Generated by Django 3.0.7 on 2020-06-18 09:54
from django.db import migrations


def create_social_links(apps, scheme_editor):
    SocialLink = apps.get_model('settings', 'SocialLink')
    for social_service_name in ('vk', 'whatsapp', 'facebook', 'viber', 'telegram', 'instagram'):
        SocialLink.objects.create(name=social_service_name)


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_auto_20200618_1254'),
    ]

    operations = [
        migrations.RunPython(create_social_links, reverse_code=migrations.RunPython.noop)
    ]
