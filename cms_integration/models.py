from ckeditor.fields import RichTextField
from django.db import models


class AboutCompanyOnIndexPage(models.Model):
    """ Index page """
    content_en = RichTextField(verbose_name='Текст на главной странице в блоке о компании на английском')
    content_ru = RichTextField(verbose_name='Текст на главной странице в блоке о компании на русском')

    class Meta:
        verbose_name_plural = 'Блок "О компании" на главной странице'

    def __str__(self):
        return 'Блок "О компании" на Главной странице. Должен быть только в 1 экземпляре.'


class ServiceText(models.Model):
    """ Service page """
    text_ru = models.TextField(verbose_name='Текст страницы услуг на русском')
    text_en = models.TextField(verbose_name='Текст страницы услуг на английском')

    class Meta:
        verbose_name_plural = 'Страница "Услуги". Текст в верху страницы'

    def __str__(self):
        return 'Текст на странице услуг. Должен быть только в 1 экземпляре.'


class Service(models.Model):
    """ Service page """
    title_en = models.CharField(max_length=255, verbose_name='Название услуг на английском')
    title_ru = models.CharField(max_length=255, verbose_name='Название услуги на русском')

    img = models.ImageField()

    content_en = RichTextField(verbose_name='Текст услуги на английском')
    content_ru = RichTextField(verbose_name='Текст услуги ан русском')

    class Meta:
        verbose_name_plural = 'Список услуг'

    def __str__(self):
        return f'{self.title_ru}. <- Эта услуга будет отображаться на странице услуг'


class AboutCompany(models.Model):
    """ About page """
    sub_title_1_en = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок 1 блока на английском',
    )
    sub_title_1_ru = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок 1 блока на русском',
    )

    body_1_en = RichTextField(verbose_name='Текст 1 блока на английском')
    body_1_ru = RichTextField(verbose_name='Текст 1 блока на русском')

    text_with_blue_background_en = RichTextField(verbose_name='Текст блока с синим фоном на английском')
    text_with_blue_background_ru = RichTextField(verbose_name='Текст блока с синим фоном на русском')

    sub_title_2_en = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок 2 блока на английском',
    )
    sub_title_2_ru = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок 2 блока на русском',
    )

    body_2_en = RichTextField(verbose_name='Текст 2 блока на английском')
    body_2_ru = RichTextField(verbose_name='Текст 2 блока на русском')

    class Meta:
        verbose_name_plural = 'Страница "О компании"'

    def __str__(self):
        return 'Настройки страницы "О компании". Должен быть только в 1 экземпляре'


class Contact(models.Model):
    """ Footer, Contacts page """
    address_ru = models.CharField(
        max_length=255,
        verbose_name='Адрес, русский'
    )
    address_en = models.CharField(
        max_length=255,
        verbose_name='Адрес, английский'
    )
    legal_address_ru = models.CharField(
        max_length=255,
        verbose_name='Юридический адрес, русский'
    )
    legal_address_en = models.CharField(
        max_length=255,
        verbose_name='Юридический адрес, английский'
    )

    working_time_ru = models.CharField(
        max_length=255,
        verbose_name='Время работы, русский'
    )
    working_time_en = models.CharField(
        max_length=255,
        verbose_name='Время работы, английский'
    )

    phone_number = models.CharField(
        max_length=255,
        verbose_name='Номера телефонов'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='email'
    )

    full_name_ru = models.CharField(
        max_length=255,
        verbose_name='Полное наименование, русский'
    )
    full_name_en = models.CharField(
        max_length=255,
        verbose_name='Полное наименование, английский'
    )

    unp = models.CharField(
        max_length=255,
        verbose_name='УНП'
    )

    class Meta:
        verbose_name_plural = 'Страница "Контакты" и "Футер"'

    def __str__(self):
        return 'Блок контактов, которые отображается в футере(нижней части экрана) и на странице "О компании". ' \
               'Должен быть только в 1 экземпляре'


class NewsSubTitle(models.Model):
    """ News page """
    sub_title_ru = models.CharField(max_length=255, verbose_name='Подзаголовок страницы новостей на русском')
    sub_title_en = models.CharField(max_length=255, verbose_name='Подзаголовок страницы новостей на английском')

    class Meta:
        verbose_name_plural = 'Страница "Новости". Текст в верху страницы'

    def __str__(self):
        return 'Подзаголовок страницы новостей. Должен быть только в 1 экземпляре.'
