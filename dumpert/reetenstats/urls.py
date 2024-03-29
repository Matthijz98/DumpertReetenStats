from django.urls import path
from . import views

urlpatterns = [
    path('', views.showsview),
    path('show/<int:show_id>', views.showview),
    path('ads.txt', views.adsview),
    path('page/over', views.aboutview, name='about'),
    path('stats/top10', views.top10view, name="top10"),
    path('stats/reeten_in_show_details', views.reeten_in_show_details)
]
