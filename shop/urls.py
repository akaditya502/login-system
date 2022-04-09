from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    
    path('', views.index,name='shop'),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('signout', views.signout,name='signout'),

    
]