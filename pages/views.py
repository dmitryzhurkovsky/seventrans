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


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()
        service_page_sub_title = ServiceSubTitle.objects.first()
        services = Service.objects.all()

        return render(
            request, template_name='services.html', context={
                'service_page_sub_title': service_page_sub_title,
                'services': services,
                'contacts': contacts
            }
        )


class ContactsView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get()

        return render(
            request, template_name='contacts.html', context={'contacts': contacts}
        )
