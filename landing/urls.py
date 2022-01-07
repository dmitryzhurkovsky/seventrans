from django.urls import path

from landing.views import (
    IndexView,
    AboutView
)

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view())
]
