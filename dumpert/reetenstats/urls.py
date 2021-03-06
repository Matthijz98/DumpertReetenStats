"""dumpert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showsview),
    path('show/dumperteeten-<int:show_id>', views.showview),
    path('api/json/ratingsinshow', views.ratinginfojsonview),
    path('api/json/top10', views.top10jsonview),
    path('api/json/shows', views.showsajaxview),
    path('ads.txt', views.adsview),
    path('page/over', views.aboutview, name='about'),
    path('stats/top10', views.top10view, name="top10"),
]
