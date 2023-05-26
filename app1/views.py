from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('dhoni is one of greatest captain')

def virat(request):
    return HttpResponse('virat is the former captain of the indian')

