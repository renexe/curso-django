from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    raise ValueError(400)
    return HttpResponse('<html><body>Hello World</body></html>', content_type='text/html')
