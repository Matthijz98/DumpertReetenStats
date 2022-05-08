from django.contrib import admin
from .models import Show, Gast, RatingType, Rating, Video


def update_dumpert_id_video(self, request, queryset):
    for video in queryset:
        video.update_dumpert_id()


class VideoAdmin(admin.ModelAdmin):
    search_fields = ["video_title"]
    actions = [update_dumpert_id_video]
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


def update_info_from_youtube(self, request, queryset):
    for show in queryset:
        show.update_info_from_youtube()


def update_info_from_dumpert(self, request, queryset):
    for show in queryset:
        show.update_info_from_dumpert()


def update_dumpert_id(self, request, queryset):
    for show in queryset:
        show.update_dumpert_id()


class ShowAdmin(admin.ModelAdmin):
    model = Show
    list_display = ["show_title", "show_date", "show_youtube_id", "show_dumpert_id", "gasten_count", "rating_sum", "video_count"]
    inlines = [RatingInlineAdmin]
    actions = [update_info_from_youtube, update_info_from_dumpert, update_dumpert_id]


# Register your models here.
admin.site.register(Show, ShowAdmin)
admin.site.register(RatingType, RatingTypeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Gast, GastAdmin)
