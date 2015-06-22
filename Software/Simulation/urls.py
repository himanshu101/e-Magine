from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^front/$', 'Simulation.views.front'),
    url(r'^quicksort/$', 'Simulation.views.quicksort'),
    url(r'^mergesort/$', 'Simulation.views.mergesort'),
    url(r'^selectionsort/$', 'Simulation.views.selectionsort'),
    url(r'^shellsort/$', 'Simulation.views.shellsort'),
    url(r'^bubblesort/$', 'Simulation.views.bubblesort'),
    url(r'^insertionsort/$', 'Simulation.views.insertionsort'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()