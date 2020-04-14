from django.shortcuts import render
from .models import Show
from django.db.models import Count, Sum

def showsview(request):
    return render(request=request,
                  template_name='reetenstats/shows.html',
                  context={"shows": Show.objects.all().order_by('-show_date').
                  annotate(num_gasten=Count('ratings_in_show__rating_by', distinct=True)).
                  annotate(total_reeten=Sum('ratings_in_show__rating_ammount')).
                  annotate(total_videos=Count('ratings_in_show__rating_video', distinct=True))})


def showview(request):
    return render(request=request,
                  template_name='reetenstats/show.html',
                  context={"show":Show.objects.filter(id=1)[0]})


