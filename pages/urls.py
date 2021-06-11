from django.urls import path
from .views import HomePageView, AboutPageView 
from django.conf import settings 

urlpatterns = [

     # new
   
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),

]

