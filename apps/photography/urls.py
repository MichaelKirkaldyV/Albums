from django.conf.urls import url
from . import views  

urlpatterns = [
  url(r'^$', views.home),
  url(r'^register_process$', views.register_process),
  url(r'^dashboard$', views.dashboard),
  url(r'^login_process$', views.login_process),
  url(r'^album$', views.add_album),
  url(r'^register$', views.register_page),
  url(r'^add_photo$', views.add_photo)
]