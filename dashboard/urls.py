from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.dashboard,name='dashboard'),
     path('results',views.result,name='results'),
     path('read-later',views.readlater,name='read-later'),
]