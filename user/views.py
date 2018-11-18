from django.shortcuts import render
from django.http import HttpResponse


def py(request):
    return HttpResponse("ok")