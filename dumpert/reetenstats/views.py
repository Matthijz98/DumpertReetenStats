from django.shortcuts import render
from .models import Show, Rating, Video, Gast
import json
from django.db.models import Avg, Sum, Count
from django.http import HttpResponse, request, Http404


def showsview(request):
    return render(request=request,
                  template_name='reetenstats/shows.html',
                  context={"shows": Show.objects.all().order_by('-show_yt_date')})


def showview(request, show_id):
    data = {"show": Show.objects.get(id=show_id)}
    return render(request=request,
                  template_name='reetenstats/show.html',
                  context=data)


def ratinginfojsonview(request,):
    show_id = request.GET.get('show')
    videos = list(dict.fromkeys(Video.objects.all().filter(rating__rating_in_show=show_id)))
    results = []

    for video in videos:
        ratings = Rating.objects.all().filter(rating_in_show=show_id).filter(rating_video=video.id).exclude(rating_type=0)
        ratings_in_video = []
        for rating in ratings:
            ratings_in_video.append({"by":rating.rating_by.gast_name,
                                     "rating_amount": str('%g'%(rating.rating_ammount)),
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


def adsview(request):
    line = "google.com, pub-1287147359957350, DIRECT, f08c47fec0942fa0"
    return HttpResponse(line)


def aboutview(request):
    return render(request=request,
                  template_name='reetenstats/about.html')


def top10view(request):
    # reeten in shows
    reeten_in_show = Rating.objects.values('rating_in_show__show_yt_title', 'rating_in_show_id').annotate(total=Sum('rating_ammount')).order_by('-total')[:10]

    # aantal reeten per gast
    reeten_by_gast = Rating.objects.values('rating_by__gast_name', 'rating_by_id').annotate(total=Sum('rating_ammount')).order_by(
        '-total')[:10]

    # meest gebruikte rating types
    most_used_rating_types = Rating.objects.values('rating_type__rating_type_name').exclude(rating_type=0).annotate(total=Sum('rating_ammount')).order_by('-total')[:10]

    # aantal reeten per video
    video_per_show = Rating.objects.values('rating_in_show__show_yt_title', 'rating_in_show_id').annotate(total=Count('rating_video', distinct=True)).order_by('-total')[:10]

    # aantal reeten per gast
    gast_in_shows = Rating.objects.values('rating_by__gast_name').annotate(total=Count('rating_in_show', distinct=True)).order_by('-total')[:10]

    # video's met de hoogste rating
    video_highest_ratings = Rating.objects.values('rating_video__video_title').annotate(total=Sum('rating_ammount')).order_by('-total')[:10]

    context = {"reeten_in_show": reeten_in_show,
               "reeten_by_gast": reeten_by_gast,
               "most_used_rating_types": most_used_rating_types,
               "video_per_show": video_per_show,
               "gast_in_shows": gast_in_shows,
               "video_highest_ratings": video_highest_ratings}

    return render(request=request,
                  template_name='reetenstats/top10.html',
                  context=context)


def reeten_in_show_details(request):
    labels = []
    data = []
    ratings = Rating.objects.values('rating_in_show__show_yt_title', 'rating_in_show_id').annotate(total=Sum('rating_ammount')).order_by('-total')

    for rating in ratings:
        labels.append(rating["rating_in_show__show_yt_title"])
        data.append(str(rating["total"]))
    return render(request=request,
                  template_name='reetenstats/reeten_in_show_details.html',
                  context={"ratings": ratings,
                           'labels': labels,
                           'data': data,
                           })
