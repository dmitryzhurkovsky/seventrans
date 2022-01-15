from django.contrib import admin

from cms_integration.models import (
    Service,
    AboutCompany,
    ServiceText,
    Contact,
    AboutCompanyOnIndexPage,
    NewsSubTitle
)

admin.site.register(AboutCompanyOnIndexPage)

admin.site.register(AboutCompany)

admin.site.register(Service)
admin.site.register(ServiceText)

admin.site.register(Contact)

admin.site.register(NewsSubTitle)



