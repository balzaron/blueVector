from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
from .models import *
from .serializers import *


class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': 1,
            'message': 'success',
            }
        return JsonResponse(d)

class PartyList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InstitutionList(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer