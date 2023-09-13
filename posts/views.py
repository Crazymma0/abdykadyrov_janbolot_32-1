from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def hello_view(request):
    return HttpResponse("Hello! It's my project")

def now_date_view(request):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current date and time: {current_date}")

def goodby_view(request):
    return HttpResponse("Goodbye, user!")
