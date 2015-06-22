from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^article', include(article.urls)),
    url(r'^edit/$','Article.views.edit_profile'),
    url(r'^login/$','Article.views.login'),
    url(r'^logout/$','Article.views.logout'),
    url(r'^chg_passwd/$', 'Article.views.change_password'),
    url(r'^passwd/$', 'Article.views.passwd'),
    url(r'^forgot_passwd/([a-zA-z0-9]{3,})/$', 'Article.views.forgot_password'),
    url(r'^forgot_chg_passwd/$', 'Article.views.forgot_change_password'),
    url(r'^add_user/$', 'Article.views.add_user'),
    url(r'^guest/$', 'Article.views.guest'),   
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()