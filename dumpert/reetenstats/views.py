from django.shortcuts import render
from .models import Show, Rating, Video
from django.db.models import Count, Sum
import json
from django.http import HttpResponse, request, Http404

def showsview(request):
    return render(request=request,
                  template_name='reetenstats/shows.html',
                  context={"shows": Show.objects.all().order_by('-show_date').
                  annotate(num_gasten=Count('ratings_in_show__rating_by', distinct=True)).
                  annotate(total_reeten=Sum('ratings_in_show__rating_ammount')).
                  annotate(total_videos=Count('ratings_in_show__rating_video', distinct=True))})


def showview(request, show_id):
    data = {"show":Show.objects.get(id=show_id)}
    return render(request=request,
                  template_name='reetenstats/show.html',
                  context=data)


def ratinginfojsonview(request,):
    show_id = request.GET.get('show')
    videos = list(dict.fromkeys(Video.objects.all().filter(rating__rating_in_show=show_id)))
    results = []

    for video in videos:
        ratings = Rating.objects.all().filter(rating_in_show=show_id).filter(rating_video=video.id)
        ratings_in_video = []
        for rating in ratings:
            ratings_in_video.append({"by":rating.rating_by.gast_name,
                                     "rating_amount": str(rating.rating_ammount),
                                     "rating_type": rating.rating_type.rating_type_name})

        results.append({
            "title": video.video_title,
            "description": video.video_description,
            "dumpert_id": video.video_dumpert_id,
            "ratings": ratings_in_video
        })


    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
