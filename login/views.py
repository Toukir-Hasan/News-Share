from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
    if request.method=="POST":
        first_name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user=User.objects.create_user(username=first_name,email=email,password=password)

        user.save()
        return render(request, "login/login.html")
    else:
        return render(request,"login/index.html")

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user= auth.authenticate(username=name,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect("/dashboard")
        else:
            return HttpResponse("Something Went Wrong!!")

    else:
        return render(request,"login/login.html")


