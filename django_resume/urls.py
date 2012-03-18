from django.conf.urls.defaults import patterns, include, url

from django_resume import views

urlpatterns = patterns('',
    url(r'^$', views.resume, name='resume'),
)