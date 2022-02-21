from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.HomePageView.as_view()),
    path('lista/', views.HomeListView.as_view()),
    path('model_lista/', views.PruebaListView.as_view()),
    path('add_view/', views.PruebaCreateView.as_view(), name='add'),
]   
