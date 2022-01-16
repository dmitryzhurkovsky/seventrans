from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from cms_integration.models import (
    AboutCompanyOnIndexPage,
    ServiceText,
    Service,
    AboutCompany,
    Contact,
    NewsSubTitle
)
from news.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()
        about_company_text_block = AboutCompanyOnIndexPage.objects.first()

        return render(
            request, template_name='index.html', context={
                'contacts': contacts,
                'about_company_text_block': about_company_text_block
            }
        )


class AboutView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()
        about_company = AboutCompany.objects.first()

        return render(
            request, template_name='about.html', context={
                'contacts': contacts,
                'about_company': about_company
            }
        )


class NewsView(ListView):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()
        news_page_sub_title = NewsSubTitle.objects.first()

        return render(
            request, template_name='news.html', context={
                'news_page_sub_title': news_page_sub_title,
                'contacts': contacts
            }
        )


class ArticleView(ListView):
    def get(self, request, pk, *args, **kwargs):
        contacts = Contact.objects.get()
        article = Article.objects.get(id=pk)

        return render(
            request, template_name='article.html', context={
                'article': article,
                'contacts': contacts
            }
        )


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()
        service_page_text = ServiceText.objects.first()

        return render(
            request, template_name='services.html', context={
                'service_page_text': service_page_text,
                'contacts': contacts
            }
        )


class ServiceView(View):
    def get(self, request, pk, *args, **kwargs):
        contacts = Contact.objects.get()
        service = Service.objects.get(id=pk)

        return render(
            request, template_name='service.html', context={
                'contacts': contacts,
                'service': service
            }
        )


class ContactsView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()

        return render(
            request, template_name='contacts.html', context={'contacts': contacts}
        )
