from django.shortcuts import render
from .models import Show, Video, RatingType, Gast, Rating
import csv
import datetime

# Create your views here.
def showsview(request):
    return render(request=request,
                  template_name='reetenstats/shows.html',
                  context={"shows": Show.objects.all()})


def showview(request):
    return render(request=request,
                  template_name='reetenstats/show.html',
                  context={"show":Show.objects.filter(id=1)[0]})


def importview(request):
    with open('../../DumpertReetenStats/data/shows.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            print(row[1])
            created = Show.objects.get_or_create(id=row[0],
                                                 show_title=row[1],
                                                 show_date=datetime.datetime.strptime(str(row[2]), "%Y-%m-%d").date(),
                                                 show_dumpert_id=row[3],
                                                 show_youtube_id=row[4],
                                                 show_description=row[5])

    with open('../../DumpertReetenStats/data/videos.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            print(row[1])
            created = Video.objects.update_or_create(id=row[0],
                                                  video_title=row[1],
                                                  video_dumpert_id=row[2],
                                                  video_description=row[3]
                                                  )

    with open('../../DumpertReetenStats/data/reeting-types.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            print(row[1])
            created = RatingType.objects.update_or_create(id=row[0],
                                                          rating_type_name=row[1])

    with open('../../DumpertReetenStats/data/gasten.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            created = Gast.objects.update_or_create(id=row[0],
                                                    gast_name=row[1],
                                                    gast_underline=row[2],
                                                    gast_website=row[7],
                                                    gast_facebook=row[8],
                                                    gast_instagram=row[9],
                                                    gast_snapchat=row[10],
                                                    gast_twitter=row[11],
                                                    gast_twitch=row[12],
                                                    gast_youtube=row[13],
                                                    gast_wiki=row[14])

    with open('../../data/reetings.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            print("id=" +row[0] +"rating_in_show_id="+str(row[1])+"rating_video_id="+str(row[2])+"rating_ammount="+str(row[3])+"rating_type_id="+str(row[4])+"rating_by_id="+str(row[5]))
            created = Rating.objects.update_or_create(
                                                      rating_in_show_id=int(row[1]),
                                                      rating_video_id=int(row[2]),
                                                      rating_ammount=float(row[3]),
                                                      rating_type_id=int(row[4]),
                                                      rating_by_id=int(row[5]))

    return render(request=request,
                  template_name='reetenstats/shows.html',
                  context={"shows": Show.objects.all()})
