from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ABD(request):
    return HttpResponse('<h1>ABD was named as the ICC ODI playes</h1>')

def Rohit(request):
    return HttpResponse('<marquee><h1>Rohit is best batsman</h1></marquee>')
