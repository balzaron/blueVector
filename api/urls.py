from django.conf.urls import url, include
from django.urls import path

from .views import *

# api url
urlpatterns = [
    # path('product/', PartyList.as_view()),
    path('user/', UserList.as_view()),
    path('institution/', InstitutionList.as_view()),
    path('agent/', AgentList.as_view()),
]