from django.shortcuts import render
from app.models import User
from app.form import NewUserForm
# Create your views here.

def index(request):
    return render(request,'app/index.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("ERROR FORM INALID")

    return render(request,'app/users.html',{'form':form})
