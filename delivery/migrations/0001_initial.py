# Generated by Django 3.0.7 on 2020-06-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Стоимость (руб.)')),
            ],
            options={
                'verbose_name': 'Способ доставки',
                'verbose_name_plural': 'Способы доставки',
            },
        ),
    ]
