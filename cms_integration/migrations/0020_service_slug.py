# Generated by Django 4.0.1 on 2022-02-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_integration', '0019_contact_instagram_href_contact_linkedin_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Название услуги в адресной строке'),
        ),
    ]