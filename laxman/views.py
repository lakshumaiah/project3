from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_laxman(request):
    return HttpResponse('<marquee><h1>hai laxman kamalakuru</marquee></h1>')
