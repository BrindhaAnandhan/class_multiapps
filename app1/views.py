from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dummy1(request):
    return render(request,"dummy_app1.html")
def dummystr(request):
    return HttpResponse("This is my string response")