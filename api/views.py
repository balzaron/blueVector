from django.http import JsonResponse

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'phone', 'deleted', )
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


class AgentLoginView(APIView):

    def post(self, request):
        user = request.data.get('name')
        pwd = request.data.get('password')

        if Agent.objects.filter(phone=user,password=pwd).first():
            return Response(r"OK")
        else:
            return Response( "Failed")

