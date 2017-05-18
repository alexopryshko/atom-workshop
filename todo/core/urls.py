from django.conf.urls import url

from core.views import index, create

urlpatterns = [
    url(r'^$', index),
    url(r'^create$', create)
]
