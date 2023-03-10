from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_ram(request):
    return HttpResponse('<marquee><h1> hai ram kamalakuru</h1></marquee>')
