from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index_view(request):
    # p
    return HttpResponse("<h1>This is home page</h1>")


def exception_view(request):
    value =12/0
    return HttpResponse("<h1>This is exception page</h1>")
