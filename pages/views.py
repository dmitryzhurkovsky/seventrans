from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from cms_integration.models import (
    AboutCompany,
    Service
)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, template_name='index.html', context={}
        )


class AboutView(View):
    def get(self, request, *args, **kwargs):
        about_company = AboutCompany.objects.first()
        return render(
            request, template_name='about.html', context={'about_company': about_company}
        )


class NewsView(ListView):
    def get(self, request, *args, **kwargs):
        return render(
            request, template_name='news.html', context={}
        )


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, template_name='services.html', context={}
        )


class ContactsView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, template_name='contacts.html', context={}
        )
