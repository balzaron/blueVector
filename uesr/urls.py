from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views



# api url
urlpatterns = [
    # url(r'^', views.index,name="home"),
    url(r'^jobs/$', views.index2, name="jobs"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
