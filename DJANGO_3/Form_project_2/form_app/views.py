from django.shortcuts import render
from . import form
# Create your views here.

def index(request):
    return render(request,'form_app/index.html')

def Form_name_view(request):
    form = form.FormName()
    return render(request,'form_app/form.html',{'form':form})
