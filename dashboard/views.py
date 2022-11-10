from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/')
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

# Create your views here.
