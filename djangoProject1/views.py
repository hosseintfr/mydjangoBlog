from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request , 'about.html')
    # return HttpResponse('hi there! I am Home now')

def home(request):
    # return HttpResponse('hi there! I am about Here')
    return render(request , 'Home.html')