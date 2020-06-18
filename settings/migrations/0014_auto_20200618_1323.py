# Generated by Django 3.0.7 on 2020-06-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_auto_20200618_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sociallink',
            options={'verbose_name': 'Ссылки на соц сети', 'verbose_name_plural': 'Ссылки на соц сети'},
        ),
        migrations.AddField(
            model_name='sociallink',
            name='show_in_navbar',
            field=models.BooleanField(default=False, verbose_name='Отображается в шапке'),
        ),
    ]
