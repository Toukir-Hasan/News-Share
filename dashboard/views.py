from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from pytrends.request import TrendReq
from . import graph
from .models import ReadLater,LikedNews,Catagory
from django.contrib.auth.models import User
from django.urls import reverse

from GoogleNews import GoogleNews

@login_required(login_url='/')
def dashboard(request):
    pytrends = TrendReq(hl='en-US')
    kw_list = ["Blockchain"]
    cat=0
    timeframe='today 5-y'
    geo=''
    gprop=''
    search_1=pytrends.realtime_trending_searches(pn='CA')
    search_ca=search_1.head(10)
    search_2=pytrends.realtime_trending_searches(pn='US')
    search_usa=search_2.head(10)
    # pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    if request.method=='POST':
        country=request.POST['country']
        search_3=pytrends.realtime_trending_searches(pn=country)
        search_new=search_3.head(10)
        return render(request, "dashboard/dashboard_modal.html",{'search_new':search_new['title']})
    return render(request, "dashboard/dashboard.html",{'search':search_ca['title'],'search_usa':search_usa['title'],})

@login_required(login_url='/')
def result(request):
    if request.method=='POST':
        a=request.POST['keywords']
        googlenews = GoogleNews(lang='en')
        googlenews.search(a)
        b=googlenews.results()
        return render(request,'dashboard/graph.html',{'chart':b})

@login_required(login_url='/')
def readlater(request):
    if request.method=="POST" :
        if request.POST.get('read')=='read':
            link=request.POST['link']
            title= request.POST['title']
            a=User.objects.get(id=request.user.id)
            read_later=ReadLater(url_name=link,title=title,name=a)
            read_later.save()
            return HttpResponseRedirect(reverse('dashboard'))
        elif request.POST.get('like')=='like':
            link=request.POST['link']
            title= request.POST['title']
            a=User.objects.get(id=request.user.id)
            like=LikedNews(url_name=link,title=title,name=a)
            like.save()
            return HttpResponseRedirect(reverse('dashboard'))
          
    else:
    
        a=request.user.id
        read_later=ReadLater.objects.filter(name__id=a)
            # read_later=ReadLater.objects.raw("select * from dashboard_ReadLater where username = 'a' ")    
        return render(request,'dashboard/readlater.html',{'read':read_later})


@login_required(login_url='/')
def catagory(request):
    a=User.objects.get(id=request.user.id)
    try:
        find=bool(Catagory.objects.get(name=a))
        return HttpResponse(find)
    except:
        return HttpResponse("jjj")
    
       
            
        
   

     
       
        
    