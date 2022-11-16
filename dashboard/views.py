from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from pytrends.request import TrendReq
from . import graph
import matplotlib.pyplot as plt
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
    pytrends = TrendReq(hl='en-US')
    if request.method=='POST':
        keywords=[]
        keywords.append(request.POST['keywords'])
        pytrends.build_payload(keywords, timeframe='today 5-y',)
        data=pytrends.interest_over_time()
        graphh=plt.plot(data)
        a= graph.get_plot(graphh)
        # return HttpResponse(keywords)
        return render(request,'dashboard/graph.html',{'chart':a})
       
        
    