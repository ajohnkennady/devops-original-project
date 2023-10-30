from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from . import views

urlpatterns = [

    path('',views.home,name='home'),    

    path('signup',views.signup,name='signup'),

    path('login_view',views.login_view,name='login_view'),

    path('logout_view',views.logout_view,name='logout_view'), 
    
    path('location',views.location,name='location'),

    path('details/<str:userId>/<str:location>', views.details, name='details'),

    path('Rise',views.Rise,name='Rise'),

    path('Accept',views.Accept,name='Accept'),

    path('notify/<str:value>/<int:id>',views.notify,name='notify'),

    path('add_blood',views.add_blood,name='add_blood'),
]