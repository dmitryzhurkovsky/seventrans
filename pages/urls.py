from django.urls import path

from pages.views import (
    IndexView,
    AboutView,
    NewsView,
    ContactsView,
    ServicesView,
    ServiceView,
    ArticleView
)

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('news/', NewsView.as_view()),
    path('news/<int:pk>/', ArticleView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('services/', ServicesView.as_view()),
    path('services/<int:pk>/', ServiceView.as_view()),
]
