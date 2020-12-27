from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def page1(request):
    return HttpResponse("You've reached the first page")
