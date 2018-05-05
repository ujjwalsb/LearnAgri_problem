from django.conf.urls import url
from farmer_data import views

urlpatterns = [
    url(r'^$', views.viewfarmerdata),
    url(r'^create/$', views.createfarmer),
    url(r'^schedule/$', views.schedule),
    url(r'^cropgrown/$', views.growingcrop),
]