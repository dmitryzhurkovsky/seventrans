from django.urls import path

from pages.views import (
    IndexView,
    AboutView,
    NewsView,
    ContactsView,
    ServicesView
)

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('news/', NewsView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('services/', ServicesView.as_view()),

]
