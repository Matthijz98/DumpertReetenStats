from django.contrib import admin
from .models import Show, Gast, RatingType, Rating, Video

# Register your models here.
admin.site.register(Show)
admin.site.register(RatingType)
admin.site.register(Rating)
admin.site.register(Video)
admin.site.register(Gast)
