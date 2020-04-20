from django.contrib import admin
from .models import Show, Gast, RatingType, Rating, Video


class VideoAdmin(admin.ModelAdmin):
    search_fields = ["video_tile"]
    list_display = ["video_title", "video_dumpert_id"]


class RatingTypeAdmin(admin.ModelAdmin):
    search_fields = ["rating_name"]


class GastAdmin(admin.ModelAdmin):
    search_fields = ["gast_name", "rating_type"]
    list_display = ["gast_name", "gast_facebook", "gast_instagram", "gast_website", "gast_snapchat", "gast_twitter", "gast_twitch", "gast_youtube", "gast_wiki"]


class RatingAdmin(admin.ModelAdmin):
    list_display = ["rating_by", "rating_in_show", "rating_ammount", "rating_type"]
    autocomplete_fields = ["rating_by", "rating_type", "rating_video"]


class RatingInlineAdmin(admin.StackedInline):
    model = Rating
    autocomplete_fields = ["rating_by", "rating_type"]


class ShowAdmin(admin.ModelAdmin):
    model = Show
    list_display = ["show_title", "show_date", "show_youtube_id", "show_youtube_id"]
    inlines = [RatingInlineAdmin]


# Register your models here.
admin.site.register(Show, ShowAdmin)
admin.site.register(RatingType, RatingTypeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Gast, GastAdmin)
