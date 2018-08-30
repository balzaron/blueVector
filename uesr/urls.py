from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views



# api url
urlpatterns = [
    # url(r'^', views.index,name="home"),
    url(r'^jobs/$', views.index, name="jobs"),
url(r'^jobList/$', views.jobList),
url(r'^jobDetail/$', views.jobDetail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
