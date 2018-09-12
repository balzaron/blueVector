from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'institution', views.InstitutionViewSet)
router.register(r'agent', views.AgentViewSet)
router.register(r'jobs', views.CourseViewSet)
router.register(r'jobdetail', views.CourseDetailViewSet)
router.register(r'lifelog', views.LifeLogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^lateststatus/$', views.LatestWorkerStatusView.as_view()),
    url(r'^agent/login$', views.AgentLoginView.as_view()),
    url(r'^jobs/$', views.index, name="jobs"),
    url(r'^jobList/$', views.jobList),
    url(r'^jobDetail/$', views.jobDetail),
    url(r'^login/$', views.login),
    url(r'^change/$', views.pw_change),
    url(r'^agentDetail/$', views.agentDetail),


]