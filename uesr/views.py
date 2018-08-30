from django.shortcuts import render
from django import template

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
def index(req):
    return render(req,"hr1/index.html")

def jobList(req):
    return render(req,'hr1/222.html')

def jobDetail(req):
    return render(req,'hr1/detail.html')