from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.

def home(request):
    return HttpResponse('Hello World')
