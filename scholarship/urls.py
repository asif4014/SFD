from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('authentication',views.authentication,name='auth'),
    path('registration', views.registration,name='registration'),
    path('saved', views.saved,name='saved'),
    path('login', views.login,name='login'),
    path('form', views.form,name='form'),
    path('form1', views.form1,name='form1'),
    path('details', views.details,name='details'),
    path('form2', views.form2,name='form2'),
    path('show', views.show,name='show'),
    path('aadharcheck', views.aadharcheck,name='aadharcheck'),
    path('usercheck', views.usercheck,name='usercheck'),
]
