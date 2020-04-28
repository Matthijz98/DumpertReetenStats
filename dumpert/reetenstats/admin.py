from django.contrib import admin
from .models import Show, Gast, RatingType, Rating, Video
import re
import requests
from bs4 import BeautifulSoup


class VideoAdmin(admin.ModelAdmin):
    search_fields = ["video_title"]
    list_display = ["video_title", "video_dumpert_id"]
    ordering = ['-id']


class RatingTypeAdmin(admin.ModelAdmin):
    search_fields = ["rating_type_name"]


class GastAdmin(admin.ModelAdmin):
    search_fields = ["gast_name"]
    list_display = ["gast_name", "gast_facebook", "gast_instagram", "gast_website", "gast_snapchat", "gast_twitter", "gast_twitch", "gast_youtube", "gast_wiki"]


class RatingAdmin(admin.ModelAdmin):
    list_display = ["rating_by", "rating_in_show", "rating_ammount", "rating_type"]
    autocomplete_fields = ["rating_by", "rating_type", "rating_video"]


class RatingInlineAdmin(admin.StackedInline):
    model = Rating
    autocomplete_fields = ["rating_by", "rating_type", "rating_video"]


def getandinsertvideos(self, request, queryset):
    for show in queryset:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', show.show_description)
        for url in urls:
            print('get info form: ' + url)
            # Get the info from this url
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            title = soup.find(class_='title')
            if title is None:
                titletext = "bestaad niet meer"
            else:
                titletext = title.text

            description = soup.find(class_='detail_description--397a1n')

            if description is None:
                descriptiontext = "bestaad niet meer"
            else:
                descriptiontext = description

            try:
                dumpertid = url.split('https://www.dumpert.nl/mediabase/')[1].rsplit('/', 1)[0]
            except IndexError:
                dumpertid = ''

            print(titletext, descriptiontext, dumpertid)
            Video.objects.get_or_create(video_title=titletext,
                                        video_description=descriptiontext,
                                        video_dumpert_id=dumpertid)


class ShowAdmin(admin.ModelAdmin):
    model = Show
    list_display = ["show_title", "show_date", "show_youtube_id", "show_dumpert_id", "gasten_count", "rating_sum", "video_count"]
    inlines = [RatingInlineAdmin]
    actions = [getandinsertvideos]


# Register your models here.
admin.site.register(Show, ShowAdmin)
admin.site.register(RatingType, RatingTypeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Gast, GastAdmin)
