from django.shortcuts import render, HttpResponse

def home(req):
    return HttpResponse('<h1>Hello World</h1>')