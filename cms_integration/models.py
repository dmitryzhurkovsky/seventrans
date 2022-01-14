from ckeditor.fields import RichTextField
from django.db import models


class SubTitleService(models.Model):
    sub_title_ru = models.CharField(max_length=255, verbose_name='Подзаголовок страницы услуг на русском')
    sub_title_en = models.CharField(max_length=255, verbose_name='Подзаголовок страницы услуг на английском')

    def __str__(self):
        return 'Подзаголовок страницы услуг. Может быть только в 1 экземпляре.'


class Service(models.Model):
    title_en = models.CharField(max_length=255, verbose_name='Название услуг на английском')
    title_ru = models.CharField(max_length=255, verbose_name='Название услуги на русском')

    img = models.ImageField()

    content_en = RichTextField(verbose_name='Текст услуги на английском')
    content_ru = RichTextField(verbose_name='Текст услуги ан русском')

    def __str__(self):
        return self.title_ru


class AboutCompany(models.Model):
    sub_title_en = models.CharField(max_length=255, verbose_name='Подзаголовк на английском', null=True, blank=True)
    sub_title_ru = models.CharField(max_length=255, verbose_name='Подзаголовок на русском', null=True, blank=True)

    body_en = RichTextField(verbose_name='Содержимое "О компании" на английском')
    body_ru = RichTextField(verbose_name='Содержимое "О компании" на русском')

    def __str__(self):
        return 'Настройки вкладки о компании. Может быть только в 1 экземпляре'
