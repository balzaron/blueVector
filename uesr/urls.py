from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views



# api url
urlpatterns = [
    url(r'^', views.index,name="home"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
