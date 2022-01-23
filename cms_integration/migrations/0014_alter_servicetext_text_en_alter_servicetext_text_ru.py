# Generated by Django 4.0.1 on 2022-01-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_integration', '0013_rename_text_with_blue_backgroun_en_aboutcompany_text_with_blue_background_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetext',
            name='text_en',
            field=models.TextField(verbose_name='Текст страницы услуг на английском'),
        ),
        migrations.AlterField(
            model_name='servicetext',
            name='text_ru',
            field=models.TextField(verbose_name='Текст страницы услуг на русском'),
        ),
    ]
