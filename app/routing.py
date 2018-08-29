from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/search/(?P<search_link>[^/]+)/$', consumers.AppConsumer),
]