from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'phone', 'deleted',  )
    # permission_classes = (permissions.IsOwnerOrReadOnly,)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',  'deleted', )


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'phone',  'deleted', )


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'phone', 'deleted', )


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'salary', 'deleted', )


class JobDetailViewSet(viewsets.ModelViewSet):
    queryset = JobDetail.objects.all()
    serializer_class = JobDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'deleted', )


class LifeLogViewSet(viewsets.ModelViewSet):
    queryset = LifeLog.objects.all()
    serializer_class = LifeLogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'deleted', )