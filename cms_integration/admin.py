from django.contrib import admin

from cms_integration.models import (
    Service,
    AboutCompany,
    ServiceSubTitle,
    Contact,
    AboutCompanyOnIndexPage,
    NewsSubTitle
)

admin.site.register(AboutCompanyOnIndexPage)

admin.site.register(AboutCompany)

admin.site.register(Service)
admin.site.register(ServiceSubTitle)

admin.site.register(Contact)

admin.site.register(NewsSubTitle)



