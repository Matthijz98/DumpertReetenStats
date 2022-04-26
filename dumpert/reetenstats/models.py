from django.db import models
from filer.fields.image import FilerImageField
from django.db.models import Count, Sum


class Gast(models.Model):
    gast_name = models.CharField(max_length=64)
    gast_underline = models.CharField(max_length=64)
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
    show_title = models.CharField(max_length=255)
    show_description = models.TextField()
    show_youtube_id = models.CharField(max_length=32)
    show_dumpert_id = models.CharField(max_length=32)
    show_date = models.DateField(null=True)

    def gasten_count(self):
        return Rating.objects.all().filter(rating_in_show = self.id).aggregate(gastencount = Count("rating_by", distinct=True))['gastencount']

    def rating_sum(self):
        return Rating.objects.all().filter(rating_in_show = self.id).aggregate(ratingsum = Sum("rating_ammount"))['ratingsum']

    def video_count(self):
        return Rating.objects.all().filter(rating_in_show = self.id).aggregate(videocount = Count("rating_video", distinct=True))['videocount']

    def __str__(self):
        return self.show_title


class Video(models.Model):
    video_title = models.CharField(max_length=255)
    video_description = models.TextField(null=True, blank=True)
    video_dumpert_id = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.video_title


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

