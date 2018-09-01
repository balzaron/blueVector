from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views



# api url
urlpatterns = [
    # url(r'^', views.index,name="home"),
    url(r'^jobs/$', views.index, name="jobs"),
url(r'^jobList/$', views.jobList),
url(r'^jobdetail/$', views.jobDetail),
url(r'^login/$', views.login),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
