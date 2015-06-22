from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^articles/$','Article.views.create'),
    url(r'^articles/all/$','Article.views.main'),
    url(r'^page=(\d{1,2})/pages/$','Article.views.main_offset'),
    url(r'^load/(\d{1,2})/$','Article.views.load_article'),
    url(r'^search/$', 'Article.views.search_titles'),
    url(r'^temp/(\d{1,2})/$', 'Article.views.load_page'),
    url(r'^myposts/all/$', 'Article.views.myposts'),
	url(r'^myposts/page=(\d{1,2})/pages/$', 'Article.views.page_offset'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()