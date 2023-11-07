from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Silk(request):
    return HttpResponse('<h1><marquee>this is not dairy milk silk</h1></marquee>')
