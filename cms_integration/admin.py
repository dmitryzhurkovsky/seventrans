from django.contrib import admin

from cms_integration.models import (
    Service,
    AboutCompany,
    SubTitleService
)

admin.site.register(Service)
admin.site.register(AboutCompany)
admin.site.register(SubTitleService)
