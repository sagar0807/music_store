from django.conf.urls import patterns, include, url
from django.views import generic
from musicapp.models import MasterDb
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^login/$', 'django.contrib.auth.views.login'),
   url(r'^$', 'musicapp.views.main', name='main'),
   url(r'^$Browse', 'musicapp.views.main', name='main'),
   url(r'^logout/$', 'django.contrib.auth.views.logout'),
   url(r'^getTopTrack/$', 'musicapp.views.getTopTrack'),
   url(r'^userPlaylists/$', 'musicapp.views.getUserPlaylist'),
   url(r'^addToPlaylist/$', 'musicapp.views.addToPlaylist'),
   url(r'^removeFromPlaylist/$', 'musicapp.views.removeFromPlaylist'),
   url(r'^addToPlaylistFromTop/$', 'musicapp.views.addToPlaylist'),
   url(r'^admin/', include(admin.site.urls)),
)
