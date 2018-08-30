from django.shortcuts import render
from django import template
from django.shortcuts import render,render_to_response

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
def index(req):
    return render(req,"hr1/index.html")

def jobList(req):
    return render(req,'hr1/222.html')

def jobDetail(req):

    print (req.GET)

    return render(req,'hr1/detail.html',req.GET)