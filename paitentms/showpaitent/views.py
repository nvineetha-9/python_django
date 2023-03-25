from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    return render(request, "register.html")

def userregister(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    username=request.POST["username"]
    email=request.POST["email"]
    password=request.POST["password1"]
    user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
    user.save()
    messages.info(request,'successfully saved')
    return render(request,"register.html")

def searchform(request):
    return render(request,"getpaitent.html")

def search(request):
    id=request.GET["id"]
    user=User.objects.get(username=id)
    print(user)
    return render(request,"getpaitent.html",{'user':user})