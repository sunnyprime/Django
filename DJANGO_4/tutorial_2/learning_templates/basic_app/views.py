from django.shortcuts import render
# from django.conf.urls.defaults import *
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context_dict = {'text':'hello World','number':100,'time':now}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/url.html')
