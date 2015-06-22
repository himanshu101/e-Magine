from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Software.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^edit/$','MyUser.views.edit_profile'),
    url(r'^login/$','MyUser.views.login'),
    url(r'^about/$', 'MyUser.views.about'),
    url(r'^logout/$','MyUser.views.logout'),    
    url(r'^forgot_passwd/([a-zA-Z0-9]{3,})/$', 'MyUser.views.forgot_password'),
    url(r'^add_user/$', 'MyUser.views.add_user'),
    url(r'^guest/$', 'MyUser.views.guest'),
    url(r'^myposts/all/$', 'MyUser.views.myposts'),
    url(r'^myposts/page=(\d{1,2})/pages/$', 'MyUser.views.page_offset'),

    url(r'^articles/$','Article.views.create'),
    url(r'^articles/all/$','Article.views.main'),
    url(r'^page=(\d{1,2})/pages/$','Article.views.main_offset'),
    url(r'^load/(\d{1,2})/$','Article.views.load_article'),
    url(r'^search/$', 'Article.views.search_titles'),
    url(r'^temp/(\d{1,2})/$', 'Article.views.load_page'),
    url(r'^sort/(\d{1,2})/$', 'Article.views.load_page1'),
    
    #url(r'^filter/$', 'Ar.views.filter'),
   
    url(r'^front/$', 'Simulation.views.front'),
    url(r'^quicksort/$', 'Simulation.views.quicksort'),
    url(r'^mergesort/$', 'Simulation.views.mergesort'),
    url(r'^selectionsort/$', 'Simulation.views.selectionsort'),
    url(r'^shellsort/$', 'Simulation.views.shellsort'),
    url(r'^bubblesort/$', 'Simulation.views.bubblesort'),
    url(r'^insertionsort/$', 'Simulation.views.insertionsort'),
    url(r'^kruskal/$', 'Simulation.views.kruskal'),
    url(r'^prim/$', 'Simulation.views.prim'),
    url(r'^dfs/$', 'Simulation.views.dfs'),
    url(r'^bfs/$', 'Simulation.views.bfs'),
    url(r'^dijkstra/$', 'Simulation.views.dijkstra'),
    url(r'^bellmann/$', 'Simulation.views.bellmann'),
    url(r'^sorttut/$', 'Simulation.views.sorttut'),
    url(r'^graphtut/$', 'Simulation.views.graphtut'),
    url(r'^fetch/([a-zA-Z0-9]{1,})/$', 'Simulation.views.temp'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
