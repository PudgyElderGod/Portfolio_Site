from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the polls.")

def home(request):
    return HttpResponse("Portfolio Home")

def contact(request):
    return HttpResponse("Contact Me")

def greet_by_name(request, name):
    return HttpResponse("Hello " + name + "!")