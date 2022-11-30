from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.dashboard,name='dashboard'),
     path('results',views.result,name='results'),
     path('results_1/<str:cat>/',views.result_1,name='results_1'),
     path('read-later',views.readlater,name='read-later'),
     path('catagory',views.catagory,name='catagory'),
]