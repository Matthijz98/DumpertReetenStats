from django.contrib import admin
from .models import Show, Gast, RatingType, Rating, Video


class VideoAdmin(admin.ModelAdmin):
    search_fields = ["video_tile"]


class RatingTypeAdmin(admin.ModelAdmin):
    search_fields = ["rating_name"]

class GastAdmin(admin.ModelAdmin):
    search_fields = ["gast_name", "rating_type"]


class RatingAdmin(admin.StackedInline):
    model = Rating
    autocomplete_fields = ["rating_by", "rating_type"]


class ShowAdmin(admin.ModelAdmin):
    model = Show
    inlines = [RatingAdmin]


# Register your models here.
admin.site.register(Show, ShowAdmin)
admin.site.register(RatingType, RatingTypeAdmin)
admin.site.register(Rating)
admin.site.register(Video, VideoAdmin)
admin.site.register(Gast, GastAdmin)
