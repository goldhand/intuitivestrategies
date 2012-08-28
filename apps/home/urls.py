from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView, TemplateView

admin.autodiscover()

urlpatterns = patterns('apps.home.views',


	url(r'^$', "Home", {"slug": "/"}), 
	
	("^admin/", include(admin.site.urls)),

)
