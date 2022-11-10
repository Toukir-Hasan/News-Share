
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
    path('index', views.index),
    path('login', views.login, name="login"),
    # path('/dashboard',views.index),
]
