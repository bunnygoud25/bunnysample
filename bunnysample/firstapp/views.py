from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hey bunny')
def detail(request):
    return HttpResponse("It is His Nickname")
