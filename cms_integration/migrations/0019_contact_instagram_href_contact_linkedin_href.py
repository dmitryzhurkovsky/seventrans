# Generated by Django 4.0.1 on 2022-02-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_integration', '0018_alter_service_preview_en_alter_service_preview_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='instagram_href',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='linkedin_href',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
