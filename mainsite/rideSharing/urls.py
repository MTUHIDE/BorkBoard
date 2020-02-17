from django.urls import path
from . import views

app_name = 'rideSharing'

#Array that contains string tokens and what to do if the token is found
urlpatterns = [
    #If the next token in the url is...

    #...blank then execute the index methon in views
    path('', views.index, name='index'),

    #...search/ then execute the search method in views
  	path('search/', views.search, name='search'),

  	#...filter/a category/ then execute the filter method in views
  	path('filter/', views.filter, name='filter'),
]
