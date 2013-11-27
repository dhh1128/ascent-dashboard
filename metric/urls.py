from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from metric import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^d3/', TemplateView.as_view(template_name="metric/d3.html")))


# vim: set et sw=4 ts=4:
