"""aviasales_hakaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from aviasales_hakaton import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

urlpatterns += i18n_patterns(
    url(r'^check-baggage/', include('check_my_baggage.urls')),

    # TODO welcome-page to download native app and view description
    # from django.urls import reverse_lazy
    # from django.views.generic import RedirectView
    # url(r'^/?$',  RedirectView.as_view(permanent=True, url=reverse_lazy('welcome'))),
    # url(r'^welcome/', include('welcome.urls')),
)
