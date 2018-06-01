
from django.conf.urls import url

from check_my_baggage.views import AirlinesListView, AirlineDetailView


urlpatterns = [
    url(r'^airlines/$', AirlinesListView.as_view()),
    url(r'^airlines/(?P<code>[A-Z]{2})/$', AirlineDetailView.as_view()),
]
