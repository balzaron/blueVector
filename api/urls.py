from django.conf.urls import url, include
from .views import *
from . import views

# api url
urlpatterns = [
    url(r'^test/$', views.GetMessageView.as_view()),
    url(r'^product/', PartyList.as_view()),
    url(r'^user/', UserList.as_view()),
    url(r'^institution/', InstitutionList.as_view())
]