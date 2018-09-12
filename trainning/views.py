from django.shortcuts import render

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


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = JobsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'salary', 'deleted','label' )


class CourseDetailViewSet(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class = JobDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'deleted', )


class LifeLogViewSet(viewsets.ModelViewSet):
    queryset = LifeLog.objects.all()
    serializer_class = LifeLogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'deleted', 'agent_phone', )


class AgentLoginView(APIView):

    def post(self, request):
        user = request.data.get('name')
        pwd = request.data.get('password')

        if Agent.objects.filter(phone=user,password=pwd).first():
            return Response(r"OK")
        else:
            return Response("Failed")


class LatestWorkerStatusView(APIView):

    def get(self, request):
        phone = request.query_params.get('agent_phone')
        deleted = request.query_params.get('deleted') or False

        phones = LifeLog.objects.distinct().values_list('phone', flat=True)
        phones = set(list(phones))
        print(phones)
        l=[]
        for p in phones:

            # obj = LifeLog.objects.filter(agent_phone=phone, deleted=deleted, phone=p).order_by('updated_time')
            # print(obj)
            obj = LifeLog.objects.filter(agent_phone=phone, deleted=deleted, phone=p).order_by('-id').first()

            if obj is not None:
                l.append(obj)
        l.sort(key=lambda k: (k.id), reverse=True)
        serializer = LifeLogSerializer(l, many=True)
        return Response(serializer.data)

from django.shortcuts import render
from django import template
from django.shortcuts import render,render_to_response

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
def index(req):
    return render(req,"train/index.html")

def jobList(req):
    return render(req,'train/222.html')

def jobDetail(req):

    print (req.GET)

    return render(req,'train/detail.html',req.GET)

def login(req):
    return render(req, 'train/login.html', req.GET)

def pw_change(req):
    return render(req, 'train/change.html', req.GET)

def agentDetail(req):
    return render(req,'train/agent_detail.html',req.GET)
