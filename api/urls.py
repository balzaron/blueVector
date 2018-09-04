from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'institution', views.InstitutionViewSet)
router.register(r'agent', views.AgentViewSet)
router.register(r'edu', views.EducationViewSet)
router.register(r'jobs', views.JobsViewSet)
router.register(r'jobdetail', views.JobDetailViewSet)
router.register(r'lifelog', views.LifeLogViewSet)
# router.register(r'agent/login', views.AgentLoginView.as_view(), base_name="agent/login")

# api url
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/$', views.LatestWorkerStatusView.as_view()),
    url(r'agent/login$', views.AgentLoginView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)

