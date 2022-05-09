import re
from django.db import models
from filer.fields.image import FilerImageField
from django.db.models import Count, Sum
from pytube import YouTube
import requests
from bs4 import BeautifulSoup


class Gast(models.Model):
    gast_name = models.CharField(max_length=64)
    gast_underline = models.CharField(max_length=64, null=True, blank=True)
    gast_age = models.DateField(null=True, blank=True)
    gast_img = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
    gast_facebook = models.URLField(null=True, blank=True)
    gast_instagram = models.URLField(null=True, blank=True)
    gast_website = models.URLField(null=True, blank=True)
    gast_snapchat = models.CharField(max_length=128, null=True, blank=True)
    gast_twitter = models.URLField(null=True, blank=True)
    gast_twitch = models.URLField(null=True, blank=True)
    gast_youtube = models.URLField(null=True, blank=True)
    gast_wiki = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.gast_name


class Show(models.Model):
    show_title = models.CharField(max_length=255, null=True, blank=True)
    show_description = models.TextField(null=True, blank=True)
    show_youtube_id = models.CharField(max_length=32, null=True, blank=True, unique=True)
    show_dumpert_id = models.CharField(max_length=32, null=True, blank=True, unique=True)
    show_date = models.DateField(blank=True, null=True)

    def gasten_count(self):
        return Rating.objects.all().filter(rating_in_show = self.id).aggregate(gastencount = Count("rating_by", distinct=True))['gastencount']

    def rating_sum(self):
        return Rating.objects.all().filter(rating_in_show = self.id).aggregate(ratingsum = Sum("rating_ammount"))['ratingsum']

    def video_count(self):
        return Rating.objects.all().filter(rating_in_show = self.id).aggregate(videocount = Count("rating_video", distinct=True))['videocount']

    def __str__(self):
        if self.show_title:
            return self.show_title
        else:
            return 'No title'

    def update_dumpert_id(self):
        if self.show_dumpert_id:
            new_id = self.show_dumpert_id.replace("/", "_", 1).replace("/", "")
            self.show_dumpert_id = new_id
            self.save()

    def update_info_from_youtube(self):
        if self.show_youtube_id:
            yt = YouTube(f'https://www.youtube.com/watch?v={self.show_youtube_id}')
            self.show_title = yt.title
            self.show_date = yt.publish_date
            self.save()

    def update_info_from_dumpert(self):
        if self.show_dumpert_id:

            URL = f"https://www.dumpert.nl/?selectedId={self.show_dumpert_id}"
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")

            results = soup.find_all("div", {"class": "description"})

            self.show_description = (results[0].decode_contents())
            self.save()

    def get_videos_from_desc(self):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.show_description)

        for url in urls:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            title = soup.find(class_='title')
            if title is None:
                titletext = "bestaad niet meer"
            else:
                titletext = str(title.text)

            description = soup.find(class_='detail_description--397a1n')

            if description is None:
                descriptiontext = "bestaad niet meer"
            else:
                descriptiontext = str(description.decode_contents())

            try:
                dumpertid = str(page.url.split('https://www.dumpert.nl/item/')[1].rsplit('/', 1)[0])
            except IndexError:
                dumpertid = ''

            Video.objects.get_or_create(video_title=titletext,
                                        video_description=descriptiontext,
                                        video_dumpert_id=dumpertid)


class Video(models.Model):
    video_title = models.CharField(null=True, blank=True, max_length=255)
    video_description = models.TextField(null=True, blank=True)
    video_dumpert_id = models.CharField(max_length=64, null=True, blank=True)
    video_override_url = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.video_title

    def update_dumpert_id(self):
        if self.show_dumpert_id:
            new_id = self.video_dumpert_id.replace("/", "_", 1).replace("/", "")
            self.video_dumpert_id = new_id
            self.save()


class RatingType(models.Model):
    rating_type_name = models.CharField(max_length=128)
    rating_type_img = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating_type_name


class Rating(models.Model):
    rating_in_show = models.ForeignKey(Show, related_name='ratings_in_show', on_delete=models.CASCADE)
    rating_by = models.ForeignKey(Gast, on_delete=models.CASCADE)
    rating_type = models.ForeignKey(RatingType, on_delete=models.CASCADE)
    rating_ammount = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    rating_video = models.ForeignKey(Video, on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.rating_in_show)

