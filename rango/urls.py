__author__ = 'AAjayKumar'

from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
    url(r'^about/$', views.about, name='about'),
    url(r'^$', views.index, name='index'),

)


