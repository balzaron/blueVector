from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'institution', views.InstitutionViewSet)
router.register(r'agent', views.AgentViewSet)
router.register(r'edu', views.EducationViewSet)
router.register(r'jobs', views.JobsViewSet)

# api url
urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
