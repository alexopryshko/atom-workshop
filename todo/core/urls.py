from django.conf.urls import url

from core.views import index, details, form_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^task/(?P<task_id>\d+)', details, name='task'),
    url(r'^form/', form_view, name='form')
]
