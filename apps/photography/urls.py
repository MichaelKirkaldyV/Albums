from django.conf.urls import url
from . import views  

urlpatterns = [
  url(r'^$', views.home),
  url(r'^register_process$', views.register_process),
  url(r'^dashboard$', views.dashboard),
  url(r'^login_process$', views.login_process),
  url(r'^register$', views.register_page),
  url(r'^add_photo/(?P<id>\d+)$', views.add_photo),
  url(r'^createAlbum$', views.createAlbum),
  url(r'^album_page/(?P<id>\d+)$', views.album_page),
  url(r'^delete_album/(?P<id>\d+)$', views.delete_album),
  url(r'^details/(?P<id>\d+)$', views.details),
  url(r'^delete/(?P<id>\d+)/(?P<album_id>\d+)$', views.delete),
  url(r'^logout/(?P<id>\d+)$', views.logout),
  url(r'^description/(?P<id>\d+)$', views.create_description),
]