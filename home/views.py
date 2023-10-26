from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('this is home page')
def about(request):
    return render(request,'about.html')
    # return HttpResponse('this is home page')
def contact(request):
    return render(request,'contact.html')
    # return HttpResponse('this is home page')
